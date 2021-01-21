class MsmeResponse:
    def __init__(self, response):
        self.response = response
        self.blocks = self.response['Blocks']
        self.name_of_enterprise_index = -1
        self.name_of_entrepreneur_index = -1
        self.type_of_organization = -1
        self.type_of_enterprise = -1
        self.is_memorandum = False
        self.parse_response()

    def parse_response(self):
        index = 0
        for block in self.blocks:
            if block['BlockType'] == 'LINE':
                if 'NAME OF ENTERPRISE' in block['Text'].upper():
                    self.name_of_enterprise_index = index + 1
                elif 'NAME OF ENTREPRENEUR' in block['Text'].upper():
                    self.name_of_entrepreneur_index = index + 1
                elif 'TYPE OF ORGANIZATION' in block['Text'].upper():
                    self.type_of_organization = index + 1
                elif 'TYPE OF ENTERPRISE' in block['Text'].upper() or 'ENTERPRISE TYPE' in block['Text'].upper():
                    self.type_of_enterprise = index + 1
                elif 'MEMORANDUM' in block['Text'].upper():
                    self.is_memorandum = True
            index = index + 1

    def fetch_name_of_enterprise(self):
        if self.name_of_enterprise_index == -1:
            return None

        return self.blocks[self.name_of_enterprise_index]['Text']

    def fetch_name_of_entrepreneur(self):
        if self.name_of_entrepreneur_index == -1:
            return None

        return self.blocks[self.name_of_entrepreneur_index]['Text']

    def fetch_type_of_organization(self):
        if self.type_of_organization == -1:
            return None

        return self.blocks[self.type_of_organization]['Text']

    def fetch_type_of_enterprise(self):
        if self.is_memorandum:
            return None
        if self.type_of_enterprise == -1:
            return None

        return self.blocks[self.type_of_enterprise]['Text']

    def create_response(self):
        result = {}

        result['enterprise_name'] = self.fetch_name_of_enterprise()
        result["entrepreneur_name"] = self.fetch_name_of_entrepreneur()
        result['type_of_organization'] = self.fetch_type_of_organization()
        result['type_of_enterprise'] = self.fetch_type_of_enterprise()

        return result
