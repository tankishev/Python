import unittest


def gen_countries(grid):
    def find_territories(cell, target, country, visited, grid):
        r, c = cell
        if r < 0 or r == len(grid):
            return
        if c < 0 or c == len(grid[0]):
            return
        if cell in visited:
            return
        if grid[r][c] != target:
            return

        visited.append(cell)
        country.append(cell)
        find_territories((r + 1, c), target, country, visited, grid)
        find_territories((r - 1, c), target, country, visited, grid)
        find_territories((r, c + 1), target, country, visited, grid)
        find_territories((r, c - 1), target, country, visited, grid)

    visited = []
    countries = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in visited:
                continue
            country = []
            target = grid[r][c]
            find_territories((r, c), target, country, visited, grid)
            if country:
                countries.append(country)

    return countries


def count_countries(grid):
    countries = gen_countries(grid)
    return len(countries)


def largest_country(grid):
    countries = gen_countries(grid)
    if countries:
        retval = sorted(countries, key=lambda x: -len(x))
        r, c = retval[0][0]
        return grid[r][c]


grid = [
    [1, 1, 2, 2, 2, 1, 1, 1],
    [1, 1, 2, 2, 2, 1, 0, 0],
    [0, 1, 1, 2, 2, 1, 1, 0],
    [0, 1, 1, 0, 2, 1, 0, 0],
    [0, 3, 3, 0, 0, 1, 2, 2],
    [0, 3, 0, 0, 3, 2, 2, 0],
    [0, 3, 3, 3, 3, 0, 0, 0],
]


class TestCountries(unittest.TestCase):
    def test_count_countries_with_one_country(self):
        self.assertEqual(count_countries([[0]]), 1)

    def test_count_countries_with_two_countries(self):
        self.assertEqual(
            count_countries(
                [[0, 0],
                 [1, 1]]
            ),
            2
        )

    def test_count_countries_diagonally_unconnected(self):
        self.assertEqual(
            count_countries(
                [[1, 0],
                 [0, 1]],
            ),
            4
        )

    def test_largest_country(self):
        self.assertEqual(
            largest_country(
                [[1, 1, 1, 1],
                 [1, 2, 2, 2],
                 [1, 1, 1, 1],
                 [0, 0, 0, 0]]
            ),
            1
        )


if __name__ == '__main__':
    unittest.main()