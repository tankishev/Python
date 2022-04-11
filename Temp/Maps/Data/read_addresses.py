from csv import reader
from DataObjects.utilities import fix_address, load_object, save_object


def read_addresses_from_csv(filepath: str, columns: tuple, header_row=False, append=None):
    data = set()

    with open(filepath, 'r') as read_obj:
        csv_reader = reader(read_obj)
        if header_row:
            header = next(csv_reader, None)
        for row in csv_reader:
            for col in columns:
                raw_address = row[col]
                if append:
                    raw_address += f', {append}'
                data.add(fix_address(raw_address))

    return [el for el in data]


def update_address_dict(filepath, update_data, overwrite=False):
    address_dict = load_object(filepath)
    if overwrite or not address_dict:
        address_dict = {}

    for el in update_data:
        if el not in address_dict.keys():
            address_dict[el] = None

    save_object(address_dict, filepath)
    return address_dict


if __name__ == '__main__':
    filename_offices = 'cc_offices.csv'
    filename_clients = 'A1_info_3.csv'
    filename_risk = 'risk_addresses.csv'

    raw_data_offices = read_addresses_from_csv(filename_offices, (0, ), append='КЕШ КРЕДИТ')
    updated_office_dict = update_address_dict('dict.offices.addresses', raw_data_offices, overwrite=True)
    print(*updated_office_dict, sep='\n')
    print(len(updated_office_dict))

    raw_data_clients = read_addresses_from_csv(filename_clients, (14, 15), header_row=True)
    updated_client_dict = update_address_dict('dict.clients.addresses', raw_data_clients, overwrite=True)
    print(*updated_client_dict, sep='\n')
    print(f'{filename_clients}:{len(updated_client_dict)}')

    raw_data_risk = read_addresses_from_csv(filename_risk, (0, ))
    updated_risk_dict = update_address_dict('dict.risk.addresses', raw_data_risk, overwrite=True)
    print(*updated_risk_dict, sep='\n')
    print(len(updated_risk_dict))
