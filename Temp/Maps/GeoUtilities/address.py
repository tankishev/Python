from abc import abstractmethod
from GeoUtilities.location import Location


class AddressLocation(Location):

    def __init__(self, address, category: str, incomplete=False):
        self.address = address
        self.category = category
        self.incomplete = incomplete

    def get_info(self):
        return {'address': self._address, 'category': self.category, 'incomplete': self.incomplete}

    @abstractmethod
    def __repr__(self):
        pass

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: str):
        if value.isspace() or type(value) != str:
            raise ValueError('Address must be a string value of minimum 3 chars')
        self._address = value


class ResidentialAddress(AddressLocation):

    def __init__(self, address: str, incomplete=False) -> None:
        super().__init__(address, 'residential', incomplete)

    def __repr__(self):
        return f'ResidentialAddress("{self.address}")'


class PermanentAddress(AddressLocation):

    def __init__(self, address: str, incomplete=False) -> None:
        super().__init__(address, 'permanent', incomplete)

    def __repr__(self):
        return f'PermanentAddress("{self.address}")'
