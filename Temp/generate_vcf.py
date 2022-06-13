from csv import reader


class Counter:

    def __init__(self, starting_num: int) -> None:
        self.starting_num = starting_num

    def __iter__(self) -> iter:
        return self

    def __next__(self):
        current_num = self.starting_num
        self.starting_num += 1
        return current_num


class VCFFile:

    def __init__(self, path: str, max_chars: int = 75) -> None:
        self.path = path
        self.max_chars = max_chars
        self.file_object = None
        self.contacts = 0

    def open(self) -> None:
        if not self.file_object:
            self.file_object = open(self.path, 'a', encoding='utf-8')

    def write_data(self, contact_data: list) -> None:
        self.file_object.write("BEGIN:VCARD\n")
        self.file_object.write("VERSION:3.0\n")
        for el in contact_data:
            data_string = el
            while len(data_string) > self.max_chars:
                text_line = data_string[0:self.max_chars]
                self.file_object.write(f"{text_line}\n")
                data_string = ' ' + data_string[self.max_chars:]
            self.file_object.write(f"{data_string}\n")
        self.file_object.write(f"END:VCARD\n")
        self.contacts += 1

    def close(self):
        self.file_object.close()
        print(f'{self.contacts} contacts added')


def main():
    file = VCFFile('python_contacts.vcf')
    file.open()

    with open('boryana_contacts_clean.csv', 'r', encoding='utf-8') as data_file:
        csv_reader = reader(data_file)
        header = next(csv_reader, None)
        for data_row in csv_reader:
            contact_data = list()
            row = ['' if el is None or el.isspace() else el for el in data_row]

            n = Counter(0)
            # read all data
            prefix = ''
            first_name = row[next(n)]
            middle_name = row[next(n)]
            last_name = row[next(n)]
            suffix = ''
            company = ''
            department = ''
            title = ''
            address_post_office = ''
            address_extended = ''
            address_street = ''
            address_locality = ''
            address_region = ''
            address_postal_code = ''
            address_country = ''
            home_address_post_office = ''
            home_address_extended = ''
            home_address_street = ''
            home_address_locality = ''
            home_address_region = ''
            home_address_postal_code = ''
            home_address_country = ''
            phone_business_fax = ''
            phone_business_1 = row[next(n)]
            phone_business_2 = ''
            phone_home_1 = row[next(n)]
            phone_home_2 = ''
            phone_mobile = row[next(n)]
            birthday = ''
            email_1 = row[next(n)]
            email_2 = ''
            email_3 = ''
            notes = row[next(n)]
            website = ''

            i = Counter(1)

            # name company and title
            formatted_name_list = [el for el in [prefix, first_name, middle_name, last_name, suffix] if el != '']
            formatted_name = ' '.join(el for el in formatted_name_list)
            name = f"{last_name};{first_name};{middle_name};{prefix};{suffix}"
            org_list = list()
            org_list.append(company)
            org_list.append(department)
            org = ';'.join(el for el in org_list)

            if name == ';;;;':
                name = company.upper()
                formatted_name = name

            contact_data.append(f"FN:{formatted_name}")
            contact_data.append(f"N:{name}")

            if org != ';':
                contact_data.append(f"ORG:{org}")
            if title != '':
                contact_data.append(f"TITLE:{title}")

            # addresses
            work_address = f"{address_post_office};{address_extended};{address_street};{address_locality};" \
                           f"{address_region};{address_postal_code};{address_country}"
            home_address = f"{home_address_post_office};{home_address_extended};" \
                           f"{home_address_street};{home_address_locality};" \
                           f"{home_address_region};{home_address_postal_code};{home_address_country}"

            if work_address != ';;;;;;':
                work_address = "ADR;TYPE=WORK:" + work_address
                contact_data.append(work_address)

            if home_address != ';;;;;;':
                home_address = "ADR;TYPE=HOME:" + home_address
                contact_data.append(home_address)

            # phones
            bus_phone_type = 'TEL;TYPE=WORK;TYPE=pref;TYPE=VOICE:'
            home_phone_type = 'TEL;TYPE=HOME;TYPE=pref;TYPE=VOICE:'
            if phone_mobile != '':
                contact_data.append(f'TEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:{phone_mobile}')
                bus_phone_type = 'TEL;TYPE=WORK;TYPE=VOICE:'
                home_phone_type = 'TEL;TYPE=HOME;TYPE=VOICE:'
            if phone_business_1 != '':
                contact_data.append(f'{bus_phone_type}{phone_business_1}')
                bus_phone_type = 'TEL;TYPE=WORK;TYPE=VOICE:'
                home_phone_type = 'TEL;TYPE=HOME;TYPE=VOICE:'
            if phone_business_2 != '':
                contact_data.append(f'{bus_phone_type}{phone_business_2}')
                home_phone_type = 'TEL;TYPE=HOME;TYPE=VOICE:'
            if phone_home_1 != '':
                contact_data.append(f'{home_phone_type}{phone_home_1}')
                home_phone_type = 'TEL;TYPE=HOME;TYPE=VOICE:'
            if phone_home_2 != '':
                contact_data.append(f'{home_phone_type}{phone_home_2}')
            if phone_business_fax != '':
                item = f'item{next(i)}'
                contact_data.append(f'{item}.TEL:{phone_business_fax}')
                contact_data.append(f'{item}.X-ABLABEL:workFax')

            # emails
            if email_1 != '':
                contact_data.append(f'EMAIL;TYPE=INTERNET:{email_1}')
            if email_2 != '':
                contact_data.append(f'EMAIL;TYPE=INTERNET:{email_2}')
            if email_3 != '':
                contact_data.append(f'EMAIL;TYPE=INTERNET:{email_3}')

            # website
            if website != '':
                item = f'item{next(i)}'
                contact_data.append(f'{item}.URL;type=pref:{website}')
                contact_data.append(f'{item}.X-ABLabel:_$!<HomePage>!$_')

            # BDay
            if birthday != '':
                month, day, year = birthday.split('/')
                if len(day) == 1:
                    day = '0' + day
                if len(month) == 1:
                    month = '0' + month
                bday = f'{year}-{month}-{day}'
                contact_data.append(f'BDAY;value=date:{bday}')

            # note
            if notes != '':
                contact_data.append(f'NOTE;CHARSET=utf-8:{notes}')

            # category
            contact_data.append('CATEGORIES:PyVCF generated')
            file.write_data(contact_data)

        file.close()


if __name__ == "__main__":
    main()

