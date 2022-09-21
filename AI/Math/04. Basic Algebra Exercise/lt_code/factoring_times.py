import secrets
import time
import matplotlib.pyplot as plt
from sympy.ntheory import factorint


def measure_time(verbose=False):
    def wrapper(func):
        def inner(*args, **kwargs):
            start = time.time()
            retval = func(*args, **kwargs)
            exec_time = time.time() - start
            if verbose:
                print(f"Function '{func.__name__}' runtime (sec): {exec_time}")
            return exec_time, retval

        return inner

    return wrapper


def list_generator(start: int, step: int, number: int) -> list:
    """
    Generates a list with 'number' of integers.
    The first one equals to 'start' and every consequtive is increased by 'step'.
    """
    i = start
    retval = [i]
    for n in range(number):
        i += step
        retval.append(i)
    return retval


@measure_time()
def get_factors(number: int) -> dict:
    return factorint(number)


@measure_time()
def multiply_factors(factors: dict) -> int:
    retval = 1
    for k, v in factors.items():
        retval *= k * v
    return retval


def get_runtimes(n_bits: int, samples: int = 1) -> tuple:
    fact_list = []
    prod_list = []

    for i in range(samples):
        number = secrets.randbits(n_bits)
        factor_time, factors = get_factors(number)
        fact_list.append(factor_time)
        multiply_time, result = multiply_factors(factors)
        prod_list.append(multiply_time)
    return sum(fact_list) / samples, sum(prod_list) / samples



def main():
    SAMPLE_SIZE = 10
    bit_sizes = [16, 32, 64, 96, 128, 160, 192]
    # bit_sizes = list_generator(, 8, 12)

    retval = []
    for n_bits in bit_sizes:
        factor_time, multiply_time = get_runtimes(n_bits, SAMPLE_SIZE)
        retval.append((n_bits, factor_time, multiply_time))

    return retval


p5_data = main()

x = [el[0] for el in p5_data]
y1 = [el[1] for el in p5_data]
y2 = [el[2] for el in p5_data]

plt.scatter(x, y1)
plt.scatter(x, y2)
plt.show()
