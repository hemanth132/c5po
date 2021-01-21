def create_gstin_response(csv):
    result = {}

    result['legal_name'] = fetch_legal_name(csv)
    result['trade_name'] = fetch_trade_name(csv)

    result['address'] = fetch_address(csv)

    return result


def fetch_legal_name(data):
    legal_name_row = data[0]
    print(legal_name_row)
    name_list = legal_name_row[2:]
    name = ' '.join(name_list)

    return name.strip()


def fetch_trade_name(data):
    trade_name = data[1]
    trade_list = trade_name[2:]
    trade_name = ' '.join(trade_list)

    return trade_name.strip()


def fetch_address(data):
    address = data[3]
    address_list = address[2:]

    print(address_list)
    address_list = list(filter(None, address_list))

    full_address = ' '.join(address_list)

    return full_address.strip()
