from rzp_ocr import app, ocr, gstinResponse
from flask import request
import boto3
import instance.config


@app.route('/ocr/start_analysis', methods=['POST'])
def start_analysis():
    content = request.get_json()

    csv = start_analysis_from_s3(content['file_name'], content['file_type'])
    return csv


@app.route('/ocr/fetch_analysis', methods=['POST'])
def fetch_analysis():
    content = request.get_json()

    csv = fetch_analysis_from_ocr(content['JobId'])

    print(type(csv))
    result = gstinResponse.create_gstin_response(csv)
    print(result)
    return result


def aws_client():
    client = boto3.client('textract',
                          aws_access_key_id=app.config["AWS_ACCESS_KEY_ID"],
                          aws_secret_access_key=app.config["AWS_SECRET_ACCESS_KEY"]
                          )

    return client


def fetch_analysis_from_ocr(job_id):
    client = aws_client()
    response = client.get_document_analysis(
        JobId=job_id
    )

    #print(response)
    blocks = response['Blocks']
    #print(blocks)

    blocks_map = {}
    table_blocks = []
    for block in blocks:
        blocks_map[block['Id']] = block
        if block['BlockType'] == "TABLE":
            table_blocks.append(block)

    if len(table_blocks) <= 0:
        return "<b> NO Table FOUND </b>"

    result = []
    for index, table in enumerate(table_blocks):
        result = ocr.generate_table_csv(table, blocks_map, index + 1)
        break

    print(result)
    print(type(result))

    # csv = ''
    # for index, table in enumerate(table_blocks):
    #     csv += ocr.generate_table_csv(table, blocks_map, index + 1)
    #     csv += '\n\n'
    #
    # return csv
    return result


def start_analysis_from_s3(file_name, fileType):
    # process using image bytes
    # get the results

    client = aws_client()
    bucket = app.config["AWS_BUCKET"]
    snsTopic = app.config["AWS_SNS_TOPIC"]
    roleAws = app.config["AWS_SNS_ROLE"]

    response = client.start_document_analysis(
        DocumentLocation={
            'S3Object': {
                'Bucket': bucket,
                'Name': file_name,
            }, },
        FeatureTypes=['TABLES'],
        JobTag=fileType,
        NotificationChannel={
            'SNSTopicArn': snsTopic,
            'RoleArn': roleAws
        },
    )

    return response
