import re

pattern = r'([^>]+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<([^>]+)'
parser = re.compile(pattern)

for _ in range(int(input())):
    password = input()
    parsed_data = parser.finditer(password)

    try:
        data = next(parsed_data)
        if data.group(1) == data.group(6):
            valid_data = data.groups()
            retval = ''.join(valid_data[1:-1])
            print(f"Password: {retval}")
        else:
            print("Try another password!")
    except StopIteration:
        print("Try another password!")
