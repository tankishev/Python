class Credit:

    def __init__(self, creditid: str, status=None, bad_flag=False) -> None:
        self.creditid = creditid
        self.status = status
        self.bad_flag = bad_flag

    def get_info(self):
        return {'creditid': self.creditid, 'status': self.status, 'is_bad': self.bad_flag}

    def __repr__(self):
        return f'Credit({self.creditid})'
