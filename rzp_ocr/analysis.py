from rzp_ocr import app, ocr
from flask import request
import boto3


@app.route('/ocr/start_analysis', methods=['POST'])
def start_analysis():
    content = request.get_json()
    return content


def get_table_csv_results_from_s3(file_name):
    # process using image bytes
    # get the results
    client = boto3.client('textract')

    response = client.start_document_analysis(
        DocumentLocation={
        'S3Object': {
            'Bucket': 'textract-console-ap-south-1-1e3d161d-8e37-4b30-9df2-f2add8139d4',
            'Name': 'string',
        }
    },
    )

    # Get the text blocks
    blocks=response['Blocks']
    pprint(blocks)

    blocks_map = {}
    table_blocks = []
    for block in blocks:
        blocks_map[block['Id']] = block
        if block['BlockType'] == "TABLE":
            table_blocks.append(block)

    if len(table_blocks) <= 0:
        return "<b> NO Table FOUND </b>"

    csv = ''
    for index, table in enumerate(table_blocks):
        csv += generate_table_csv(table, blocks_map, index +1)
        csv += '\n\n'

    return csv
