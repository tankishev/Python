import numpy as np
import matplotlib.pyplot as plt
import math


def gen_main_grid(grid_size: int) -> tuple:
    """
    The function returns a tuple of arrays with coordinates for each pixel
    """
    side = np.arange(0, grid_size, 1)
    x_axis = np.tile(side, grid_size)
    y_axis = np.repeat(side, grid_size)
    return x_axis, y_axis


def gen_grad_grid(main_grid_size: int, granularity=1) -> tuple:
    """
    This fucnction makes sure that the main grid size can be split to the chosen granularity
    """
    while main_grid_size % granularity != 0:
        granularity -= 1
    grad_grid_size = int(main_grid_size / granularity)
    return granularity, grad_grid_size


def generate_gradient_vectors_matrix(number_of_unique_vectors: int, gradient_grid_size: int) -> np.ndarray:
    v = np.linspace(0, 2 * np.pi, number_of_unique_vectors + 1)
    vy = np.round(np.sin(v), 5)
    vx = np.round(np.cos(v), 5)
    vectors = tuple(zip(vx, vy))

    vector_indexes = list(range(number_of_unique_vectors))
    random_indexes = np.random.choice(vector_indexes, size=gradient_grid_size ** 2)

    return np.array([vectors[idx] for idx in random_indexes]).reshape([gradient_grid_size, gradient_grid_size, 2])


def fade_noise(x):
    return x**5 * 6 - x**4 * 15 + x**3 * 10


def calc_gradient(x: int, y: int, dm: np.ndarray, gvc: np.ndarray, gvm: list):
    """
    This fucntion calculates the gradient value for a given pixel (cell).

    Args:
        x, y (int): the x and y coordinates of the cell in the main grid
        dm (numpy.ndarray): an array with the relative distance matrix for the gradient grid
        gvc (numpy.ndarray): an array with the coordinates of the lower left gradient vector for this pixel
        gvm (list): the matrix with gradient distance vectors
    """

    # Calc the relative location of the cell in the dm
    xloc, yloc = x % len(dm), y % len(dm)

    # Calc the distance vectors (bottom left, bottom right, top left, top right)
    dbl = np.array([dm[xloc], dm[yloc]])
    dbr = np.array([dm[xloc] - 1, dm[yloc]])
    dtl = np.array([dm[xloc], dm[yloc] - 1])
    dtr = np.array([dm[xloc] - 1, dm[yloc] - 1])

    # Get the gradient vector (gvc = gradient vector coordinates for the bottom left vector)
    gbl = gvm[gvc[0]][gvc[1]]
    gbr = gvm[gvc[0] + 1][gvc[1]]
    gtl = gvm[gvc[0]][gvc[1] + 1]
    gtr = gvm[gvc[0] + 1][gvc[1] + 1]

    # Calc dot product
    dpbl = np.dot(dbl, gbl)
    dpbr = np.dot(dbr, gbr)
    dptl = np.dot(dtl, gtl)
    dptr = np.dot(dtr, gtr)

    l1 = dpbl + (dpbr - dpbl) * fade_noise(dm[xloc])
    l2 = dptl + (dptr - dptl) * fade_noise(dm[xloc])
    result = l1 + (l2 - l1) * fade_noise(dm[yloc])

    return result


if __name__ == '__main__':
    main_grid_size = 128
    set_granularity = 3
    set_number_unique_vectors = 8

    x, y = gen_main_grid(main_grid_size)
    granularity, grad_grid_size = gen_grad_grid(main_grid_size, set_granularity)
    gvm = generate_gradient_vectors_matrix(set_number_unique_vectors, grad_grid_size)
    dm = np.linspace(0, 1, grad_grid_size)

    # Calc gradient vectors coordinates for each cell
    g_c = np.vectorize(lambda n, s: math.floor(n / s))
    gx = np.array(g_c(x, grad_grid_size))
    gy = np.array(g_c(y, grad_grid_size))
    gc = np.vstack((gx, gy)).T

    gradient = [calc_gradient(x[i], y[i], dm, gc[i], gvm) for i in range(main_grid_size ** 2)]
    gradient = np.reshape(gradient, [main_grid_size, main_grid_size])

    plt.imshow(gradient)
    plt.gca().invert_yaxis()
    plt.show()
