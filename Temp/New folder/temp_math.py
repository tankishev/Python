import pickle
import struct

def read_object_from_file(filename: str):
    try:
        with open(filename, 'rb') as file:
            read_object = pickle.load(file)
        return read_object
    except FileNotFoundError:
        return None


if __name__ == '__main__':

    filename = 'advanced-potion-making'
    # data = read_object_from_file(filename)
    f = open(filename, "rb")
    data = f.read()
    i = int.from_bytes(data[:4], byteorder='little', signed=False)
    ints = struct.unpack('iiii', data[:16])
    (eight, N) = struct.unpack("@II", data)
    data_bin = []
