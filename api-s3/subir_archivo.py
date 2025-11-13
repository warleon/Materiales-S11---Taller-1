import boto3
import base64


def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event["body"]["bucket"]
    nombre_directorio = event["body"]["directorio"]
    nombre_archivo = event["body"]["archivo"]
    contenido = event["body"]["contenido"]  # base64

    # Proceso
    s3 = boto3.client("s3")
    decoded_file = base64.b64decode(contenido)
    s3.put_object(
        Bucket=nombre_bucket,
        Key=f"{nombre_directorio}/{nombre_archivo}",
        Body=decoded_file,
    )

    # Salida
    return {
        "statusCode": 200,
        "mensaje": f'Archivo "{nombre_archivo}" subido correctamente al directorio "{nombre_directorio}" en el bucket "{nombre_bucket}".',
    }
