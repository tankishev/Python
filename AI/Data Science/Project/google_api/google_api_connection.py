from abc import ABC, abstractmethod


class GoogleAPIConnection(ABC):
    _API_KEY = 'PUT YOUR GOOGLE API KEY HERE'

    @abstractmethod
    def __init__(self):
        pass
