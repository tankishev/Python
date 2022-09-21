import secrets
from sympy.ntheory import primefactors
from prime_generator import is_prime


class Connection:

    def __init__(self, pbk_nbits: int) -> None:
        self.pbk_nbits = pbk_nbits
        self.pbk = self.__gen_pbk()
        self.messages = []

    def send_message(self, sender_name: str, message: str) -> None:
        self.messages.append((sender_name, message))

    def __gen_pbk(self) -> tuple:
        p = self.__gen_prime()
        pf = primefactors(p - 1)
        for n in range(2, p):
            is_primitive = True
            if any(n ** ((p-1)//i) % p == 1 for i in pf):
                is_primitive = False
            if is_primitive:
                return p, n

    def __str__(self):
        return f'Connection public key (prime, base): {self.pbk}'

    def __gen_prime(self) -> int:
        while True:
            n = secrets.randbits(self.pbk_nbits)
            if n % 2 == 0:
                continue
            if is_prime(n):
                return n
