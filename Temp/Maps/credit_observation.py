from locations import AddressLocation


class Credit:

    def __init__(self, creditid: str, status=None, bad_flag=False) -> None:
        self.creditid = creditid
        self.status = status
        self.bad_flag = bad_flag

    def get_info(self):
        return {'creditid': self.creditid, 'status': self.status, 'is_bad': self.bad_flag}

    def __repr__(self):
        return f'Credit({self.creditid})'


class Observation:

    def __init__(self, credit: Credit, address: AddressLocation) -> None:
        self.credit = credit
        self.address = address
        self.google_address = None

    def get_info(self):
        return f'Credit: {self.credit.get_info()}\n' \
               f'Address: {self.address.get_info()}\n' \
               f'GoogleInfo: {self.google_address.get_info()}'
