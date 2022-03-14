import unittest


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class IntegerListTests(unittest.TestCase):

    def test_constructor(self):
        input_list = [2, -3, 4]
        il = IntegerList(*input_list)
        self.assertTrue(hasattr(il, f'_{il.__class__.__name__}__data'))
        self.assertListEqual(getattr(il, f'_{il.__class__.__name__}__data', None), input_list)

    def test_only_integers_are_stored_at_init(self):
        il = IntegerList('2', -3, 'a')
        expected = [-3]
        self.assertListEqual(getattr(il, f'_{il.__class__.__name__}__data', None), expected)

    def test_all_required_methods_exist(self):
        il = IntegerList(2, -3, 4)
        self.assertTrue(hasattr(il, 'add') and callable(getattr(il, 'add', None)))
        self.assertTrue(hasattr(il, 'get_data') and callable(getattr(il, 'get_data', None)))
        self.assertTrue(hasattr(il, 'remove_index') and callable(getattr(il, 'remove_index', None)))
        self.assertTrue(hasattr(il, 'get') and callable(getattr(il, 'get', None)))
        self.assertTrue(hasattr(il, 'insert') and callable(getattr(il, 'insert', None)))
        self.assertTrue(hasattr(il, 'get_biggest') and callable(getattr(il, 'get_biggest', None)))
        self.assertTrue(hasattr(il, 'get_index') and callable(getattr(il, 'get_index', None)))

    def test_get_data_returns_correct_data(self):
        il = IntegerList(2, -3, 4)
        self.assertEqual(il.get_data(), [2, -3, 4])

    def test_add_method_adds_element_and_returns_correct_list(self):
        il = IntegerList(2, -3, 4)
        self.assertListEqual(il.add(-10), [2, -3, 4, -10])

    def test_add_data_adds_only_integers_to_list(self):
        il = IntegerList(2, -3, 4)
        try:
            il.add('4')
        except ValueError:
            self.assertListEqual(il.get_data(), [2, -3, 4])

    def test_add_data_returns_value_error_for_non_integers(self):
        il = IntegerList(2, -3, 4)
        with self.assertRaises(ValueError) as context:
            il.add('5')
        self.assertTrue('Element is not Integer' in str(context.exception))

    def test_remove_index_returns_correct_element(self):
        il = IntegerList(2, -3, 4)
        actual = il.remove_index(1)
        self.assertEqual(actual, -3)

    def test_remove_index_returns_index_error_when_out_of_range(self):
        il = IntegerList(2, -3, 4)
        with self.assertRaises(IndexError) as context:
            il.remove_index(5)
        self.assertTrue('Index is out of range' in str(context.exception))

    def test_remove_index_removes_element_from_list(self):
        il = IntegerList(2, -3, 4)
        il.remove_index(1)
        self.assertListEqual(il.get_data(), [2, 4])

    def test_get_returns_correct_element(self):
        il = IntegerList(2, -3, 4)
        self.assertEqual(il.get(1), -3)

    def test_get_returns_index_error_on_index_out_of_range(self):
        il = IntegerList(2, -3, 4)
        with self.assertRaises(IndexError) as context:
            il.get(5)
        self.assertTrue('Index is out of range' in str(context.exception))

    def test_insert_adds_only_integers_and_raises_value_error_if_not(self):
        il = IntegerList(2, -3, 4)
        expected = [2, -3, 4]
        with self.assertRaises(ValueError) as context:
            il.insert(1, '5')
        self.assertTrue('Element is not Integer' in str(context.exception))
        self.assertListEqual(getattr(il, f'_{il.__class__.__name__}__data', None), expected)

    def test_insert_adds_element_at_correct_index(self):
        il = IntegerList(2, -3, 4)
        il.insert(1, 5)
        data_lst = getattr(il, f'_{il.__class__.__name__}__data', None)
        actual = data_lst[1]
        self.assertEqual(actual, 5)

    def test_insert_returns_index_error_on_index_out_of_range(self):
        il = IntegerList(2, -3, 4)
        with self.assertRaises(IndexError) as context:
            il.insert(5, 5)
        self.assertTrue('Index is out of range' in str(context.exception))

    def test_get_methods_not_changing_the_list(self):
        il = IntegerList(2, -3, 4)
        expected = [2, -3, 4]
        il.get_data()
        il.get(0)
        il.get_index(2)
        il.get_biggest()
        self.assertListEqual(getattr(il, f'_{il.__class__.__name__}__data', None), expected)

    def test_get_biggest_returns_correct_value(self):
        il = IntegerList(2, -3, 4)
        expected = 4
        actual = il.get_biggest()
        self.assertEqual(actual, expected)

    def test_get_index_returns_correct_value(self):
        il = IntegerList(2, -3, 4)
        expected = 2
        actual = il.get_index(4)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
