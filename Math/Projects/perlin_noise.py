import math
import matplotlib.pyplot as plt
import numpy as np


def gen_main_grid(grid_size: int) -> tuple:
    side = np.arange(0, grid_size, 1)
    x_axis = np.tile(side, grid_size)
    y_axis = np.repeat(side, grid_size)
    return x_axis, y_axis


def gen_grad_grid(main_grid_size: int, granularity=1) -> tuple:
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

    # vectors = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    # vector_indexes = list(range(len(vectors)))
    random_indexes = np.random.choice(vector_indexes, size=gradient_grid_size**2)
    output = np.array([vectors[idx] for idx in random_indexes]).reshape([gradient_grid_size, gradient_grid_size, 2])
    # print(output)
    return output


def calc_gradient(x: int, y: int, dm: np.ndarray, gvc: np.ndarray, gvm: list):
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
    result = l1 + (l2-l1) * fade_noise(dm[yloc])
    # dm[yloc]
    return result


def fade_noise(x):
    return x**5 * 6 - x**4 * 15 + x**3 * 10


def generate_noise(main_grid_size, sub_grid_number, gvm):

    # Generate main grid, gradient vectors matrix and distance array
    x, y = gen_main_grid(main_grid_size)
    while main_grid_size % sub_grid_number != 0:
        sub_grid_number -= 1
    grad_grid_size = int(main_grid_size / sub_grid_number)

    dm = np.linspace(0, 1, grad_grid_size)

    # Calc gradient vectors coordinates for each cell
    g_c = np.vectorize(lambda n, s: math.floor(n / s))
    gx = np.array(g_c(x, grad_grid_size))
    gy = np.array(g_c(y, grad_grid_size))
    gc = np.vstack((gx, gy)).T

    gradient = [calc_gradient(x[i], y[i], dm, gc[i], gvm) for i in range(main_grid_size ** 2)]

    return gradient


def gen_images_effect_of_details(img_size: int, sub_grids_number: int, detail_levels: int):

    gvm = generate_gradient_vectors_matrix(8, 2 ** sub_grids_number + 1)
    gr = np.array(generate_noise(img_size, 2 ** sub_grids_number, gvm))

    # Plotting 4 images next ot each other
    grx = np.reshape(gr, [img_size, img_size])
    f, axarr = plt.subplots(1, detail_levels + 1)
    axarr[0].set_title(f"Base layer")
    axarr[0].imshow(grx)
    axarr[0].invert_yaxis()

    if detail_levels > 0:
        for i in range(1, detail_levels + 1):
            detail_level = sub_grids_number + i
            gvo = generate_gradient_vectors_matrix(8, 2 ** detail_level + 1)
            gro = np.array(generate_noise(img_size, 2 ** detail_level, gvo))
            gr += gro / 2 ** detail_level

            # Plotting 4 octaves next to each other
            grx = np.reshape(gr, [img_size, img_size])
            axarr[i].set_title(f"Add details {i}")
            axarr[i].imshow(grx)
            axarr[i].invert_yaxis()

    plt.show()


def gen_images_effect_of_number_of_sub_grids(img_size: int, min_sub_grids: int, grid_levels=0):

    if grid_levels > 0:
        f, axarr = plt.subplots(1, grid_levels + 1)
    else:
        plt.title(f"Gradient sub grid {min_sub_grids + 1}x{min_sub_grids + 1}")

    for i in range(grid_levels + 1):
        sub_grids_num = min_sub_grids + i
        gvm = generate_gradient_vectors_matrix(8, 2 ** sub_grids_num + 1)
        gr = np.array(generate_noise(img_size, 2 ** sub_grids_num, gvm))
        gr = np.reshape(gr, [img_size, img_size])
        if grid_levels > 0:
            axarr[i].set_title(f"Gradient sub grid {sub_grids_num + 1}x{sub_grids_num + 1}")
            axarr[i].imshow(gr)
            axarr[i].invert_yaxis()
        else:
            plt.imshow(gr)
            plt.gca().invert_yaxis()

    plt.show()


def final_script(main_grid_size=128, starting_gran=1, gran_levels=3, num_unique_vectors=8):
    x, y = gen_main_grid(main_grid_size)
    for i in range(starting_gran, starting_gran + gran_levels):
        granularity, grad_grid_size = gen_grad_grid(main_grid_size, i)
        gvm = generate_gradient_vectors_matrix(num_unique_vectors, grad_grid_size)
        dm = np.linspace(0, 1, grad_grid_size)


def main_scipt():
    img_size = 256
    base_frequency = 1
    octaves = 3

    gvm = generate_gradient_vectors_matrix(8, 2 ** base_frequency + 1)
    gr = np.array(generate_noise(img_size, 2 ** base_frequency, gvm))

    # Plotting 4 images next ot each other
    grx = np.reshape(gr, [img_size, img_size])
    f, axarr = plt.subplots(1, 4)
    axarr[0].set_title("")
    axarr[0].imshow(grx)

    if octaves > 0:
        for i in range(1, octaves + 1):
            frequency = base_frequency + i
            gvo = generate_gradient_vectors_matrix(8, 2 ** frequency + 1)
            gro = np.array(generate_noise(img_size, 2 ** frequency, gvo))
            gr += gro / 2**frequency

            # Plotting 4 octaves next to each other
            grx = np.reshape(gr, [img_size, img_size])
            axarr[i].imshow(grx)

    # Standard plot
    # gr = np.reshape(gr, [img_size, img_size])
    # plt.imshow(gr)

    # Plotting on a 3d field with terrain colors
    # x = range(img_size)
    # y = range(img_size)
    #
    # hf = plt.figure()
    # ha = hf.add_subplot(111, projection='3d')
    #
    # X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` data to be 2D
    # ha.plot_surface(X, Y, gr, cmap='terrain')
    #
    plt.show()


def fully_random_generation(size):
    arr = np.random.rand(size ** 2)
    arr = arr.reshape([size, size])
    plt.imshow(arr)
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == '__main__':
    # gen_images_effect_of_details(256, 3, 1)
    gen_images_effect_of_number_of_sub_grids(256, 3, 0)
    # fully_random_generation(256)