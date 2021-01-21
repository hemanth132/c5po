import json

def create_msme_response(csv):
    result = {}

    result['enterprise_name'] = fetch_name_of_enterprise(csv)
    result["entrepreneur_name"] = fetch_name_of_entrepreneur(csv)
    result['type_of_organization'] = fetch_type_of_organization(csv)
    result['type_of_enterprise'] = fetch_type_of_enterprise(csv)

    return result


def fetch_name_of_enterprise(data):
    blocks = data['Blocks']
    textBlock = []
    index = 0
    name_of_enterprise_index = 0
    print(type(blocks))
    for block in blocks:
        if block['BlockType'] == 'LINE':
            text = block['Text']
            # print(text)
            if 'NAME OF ENTERPRISE' in text.upper():
                textBlock = block
                name_of_enterprise_index = index + 1
        index = index + 1

    name_print = blocks[name_of_enterprise_index]

    if 'Text' in name_print:
        return name_print['Text']
    return None




def fetch_name_of_entrepreneur(data):
    blocks = data['Blocks']
    textBlock = []
    index = 0
    type_of_enterprise_index = 0
    print(type(blocks))
    for block in blocks:
        if block['BlockType'] == 'LINE':
            text = block['Text']
            if 'NAME OF ENTREPRENEUR' in text.upper():
                print(block)
                textBlock = block
                type_of_enterprise_index = index + 1
        index = index + 1

    name_print = blocks[type_of_enterprise_index]

    if 'Text' in name_print:
        return name_print['Text']
    return None


def fetch_type_of_organization(data):
    blocks = data['Blocks']
    textBlock = []
    index = 0
    type_of_enterprise_index = 0
    print(type(blocks))
    for block in blocks:
        if block['BlockType'] == 'LINE':
            text = block['Text']
            print(text)
            if 'TYPE OF ORGANIZATION' in text.upper():
                print(block)
                textBlock = block
                type_of_enterprise_index = index + 1
        index = index + 1

    name_print = blocks[type_of_enterprise_index]

    if 'Text' in name_print:
        return name_print['Text']
    return None


def fetch_type_of_enterprise(data):

    blocks = data['Blocks']
    textBlock = []
    index = 0
    type_of_enterprise_index = 0
    print(type(blocks))
    for block in blocks:
        if block['BlockType'] == 'LINE':
            text = block['Text']
            if 'MEMORANDUM' in text.upper():
                return None

            if 'TYPE OF ENTERPRISE' in text.upper() or 'ENTERPRISE TYPE' in text.upper():
                print(block)
                textBlock = block
                type_of_enterprise_index = index + 1
        index = index + 1

    name_print = blocks[type_of_enterprise_index]

    if 'Text' in name_print:
        return name_print['Text']
    return None


def fetchKeys(data):
    blocks = data['Blocks']
    textBlock = []
    index = 0
    name_of_enterprise_index = 0
    print(type(blocks))
    for block in blocks:
        if block['BlockType'] == 'LINE':
            text = block['Text']
            if text == 'NAME OF ENTERPRISE':
                print(block)
                textBlock = block
                name_of_enterprise_index = index+1
        index = index+1


    name_print = blocks[name_of_enterprise_index]

    print(name_print['Text'])


    return name_print['Text']



