from connection import Connection, secrets


class User:

    def __init__(self, name: str) -> None:
        self.name = name
        self.connection = None
        self.keys = dict()

    def connect(self, connection: Connection) -> None:
        if self.connection != connection:
            self.connection = connection
            self.keys.clear()
            self.generate_keys()

    def generate_keys(self) -> None:
        if self.connection:
            p, g = self.connection.pbk
            pk = secrets.randbelow(p)
            pbk = g ** pk % p
            self.keys['private'] = pk
            self.keys['public'] = pbk

    def exchange_pbk(self) -> None:
        if self.connection:
            pbk = self.keys.get('public')
            self.connection.send_message(self.name, f'pbk:{pbk}')

    def generate_sk(self):
        if self.connection:
            messages = [msg for sender, msg in self.connection.messages if sender != self.name]
            other_pbk = next(el.split(':')[1] for el in messages if 'pbk:' in el)
            if other_pbk:
                p = self.connection.pbk[0]
                pk = self.keys.get('private')
                sk = (int(other_pbk) ** pk) % p
                self.keys['shared'] = sk

    def __str__(self):
        return f'\nUser: {self.name}' \
               f'\nKeys: {self.keys}'
