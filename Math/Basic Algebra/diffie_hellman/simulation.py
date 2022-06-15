from connection import Connection
from user import User
from time import time


class Simulation:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.users = []

    def add_person(self, name: str):
        if name not in [user.name for user in self.users]:
            self.users.append(User(name))

    def generate_sks(self, verbose=False):
        start = time()
        for user in self.users:
            user.connect(self.connection)
            user.exchange_pbk()
        for user in self.users:
            user.generate_sk()
            if verbose:
                print(user)
        exec_time = time() - start
        if verbose:
            print(f"Time to generate shared keys (sec): {exec_time}")

    def crack_sk(self, verbose=False):
        start = time()
        pbks = {user.name: user.keys.get('public') for user in self.users}
        p, g = self.connection.pbk
        for pk_guess in range(1, p):
            pbk = g ** pk_guess % p
            if pbk in pbks.values():
                exec_time = time() - start
                if verbose:
                    username = next(name for name, key in pbks.items() if key == pbk)
                    other_pbk = next(item for item in pbks.values() if item != pbk)
                    sk = other_pbk ** pk_guess % p
                    print(f"Found {username}'s pk: {pk_guess}")
                    print(f"Shared key: {sk}")
                    print(f"Time to find shared key (sec): {exec_time}")
                return exec_time


def run_sims(bits, attempts, verbose=False):
    results = []
    for i in range(attempts):
        conn = Connection(bits)
        if verbose:
            print(conn)
        sim = Simulation(conn)
        sim.add_person('Alice')
        sim.add_person('Bob')
        sim.generate_sks(verbose)
        results.append(sim.crack_sk(verbose))
    return results


if __name__ == '__main__':
    attempts = 5
    results = run_sims(16, attempts, True)
    print(f'Average crack time: {sum(results) / attempts}')
