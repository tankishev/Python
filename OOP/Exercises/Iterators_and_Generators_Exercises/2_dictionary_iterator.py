class dictionary_iter:

    def __init__(self, dict_obj: dict) -> None:
        self.dict_obj = dict_obj

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> tuple:
        if self.dict_obj.keys():
            key = list(self.dict_obj.keys())[0]
            value = self.dict_obj.pop(key)
            return key, value
        raise StopIteration()


if __name__ == '__main__':
    result = dictionary_iter({1: "1", 2: "2"})
    for x in result:
        print(x)
