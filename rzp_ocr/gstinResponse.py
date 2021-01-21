from rzp_ocr import tables_helper


class GstinResponse:
    def __init__(self, response):
        self.response = response
        self.table_block_ids = []
        self.tables_text = {}
        self.parse_response()

    def parse_response(self):
        blocks = self.response['Blocks']

        blocks_map = {}
        for block in blocks:
            blocks_map[block['Id']] = block
            if block['BlockType'] == "TABLE":
                self.table_block_ids.append(block['Id'])

        for blockId in self.table_block_ids:
            self.tables_text[blockId] = tables_helper.get_rows_columns_map(blocks_map[blockId], blocks_map)

        # print(self.table_block_ids)
        # print(self.tables_text)

    def fetch_legal_name(self):
        first_table_id = self.table_block_ids[0]
        table = self.tables_text[first_table_id]

        row = table[1]
        name_list = tables_helper.get_columns_array_after_index(row, 2)
        name = ' '.join(name_list).strip()

        return name

    def fetch_trade_name(self):
        first_table_id = self.table_block_ids[0]
        table = self.tables_text[first_table_id]

        trade_name = table[2]
        trade_list = tables_helper.get_columns_array_after_index(trade_name, 2)
        trade_name = ' '.join(trade_list).strip()

        return trade_name

    def fetch_address(self):
        first_table_id = self.table_block_ids[0]
        table = self.tables_text[first_table_id]

        address = table[4]
        address_list = tables_helper.get_columns_array_after_index(address, 2)

        address_list = list(filter(None, address_list))

        full_address = ' '.join(address_list).strip()

        return full_address

    def create_response(self):
        result = {'legal_name': self.fetch_legal_name(), 'trade_name': self.fetch_trade_name(),
                  'address': self.fetch_address()}

        return result
