from rzp_ocr import app, gstinResponse, aws, msmeResponse, tables_helper
from flask import request


@app.route('/ocr/start_analysis', methods=['POST'])
def start_analysis():
    content = request.get_json()

    response = aws.textract_start_analysis(content['file_name'], content['file_type'], ['TABLES'])
    return response


@app.route('/ocr/fetch_analysis', methods=['POST'])
def fetch_analysis():
    content = request.get_json()

    response = aws.textract_fetch_analysis(content['JobId'])

    # check if in progress
    if response['JobStatus'] == 'IN_PROGRESS':
        return response

    if content['file_type'] == 'gst':
        result = gstinResponse.GstinResponse(response).create_response()
    else:
        result = msmeResponse.MsmeResponse(response).create_response()

    # print(result)
    return result
