import boto3


def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event["body"]["bucket"]
    nombre_directorio = event["body"]["directorio"]

    # Proceso: en S3 los "directorios" son claves que terminan en '/'
    s3 = boto3.client("s3")
    s3.put_object(Bucket=nombre_bucket, Key=f"{nombre_directorio}/")

    # Salida
    return {
        "statusCode": 200,
        "mensaje": f'Directorio "{nombre_directorio}/" creado en el bucket "{nombre_bucket}".',
    }
