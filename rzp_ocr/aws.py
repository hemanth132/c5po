from rzp_ocr import app
import boto3


def aws_client():
    client = boto3.client('textract',
                          aws_access_key_id=app.config["AWS_ACCESS_KEY_ID"],
                          aws_secret_access_key=app.config["AWS_SECRET_ACCESS_KEY"]
                          )

    return client


def textract_start_analysis(file_name, file_type, feature_types):
    client = aws_client()
    bucket = app.config["AWS_BUCKET"]
    sns_topic = app.config["AWS_SNS_TOPIC"]
    role_aws = app.config["AWS_SNS_ROLE"]

    response = client.start_document_analysis(
        DocumentLocation={
            'S3Object': {
                'Bucket': bucket,
                'Name': file_name,
            }, },
        FeatureTypes=feature_types,
        JobTag=file_type,
        NotificationChannel={
            'SNSTopicArn': sns_topic,
            'RoleArn': role_aws
        },
    )

    return response


def textract_fetch_analysis(job_id):
    client = aws_client()
    response = client.get_document_analysis(
        JobId=job_id
    )

    return response
