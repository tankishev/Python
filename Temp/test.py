import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def fully_random_generation(size):
    arr = np.random.rand(size ** 2)
    arr = arr.reshape([size, size])
    plt.imshow(arr)
    plt.gca().invert_yaxis()
    plt.title("Fig.1: Fully random noise")
    plt.show()


fully_random_generation(256)


def gen_distance_vectors(size: int, elements: int):
    """
    This functoin generates a distance matrix for each pixel.
    Inputs:
        size: int - pixels per row in the image
        elements: int - pixels per row in each subgrid
    """
    D = np.zeros((2, size, size))
    if elements == 1:
        return D

    A = np.tile(np.arange(size), size).reshape((size, size))

    D[0] = (D[0, :, :] + A % elements) / (elements - 1)
    D[1] = D[0].T

    D = np.flip(D, 1)
    return D


# Example
s = 6
DV = gen_distance_vectors(s, 3)
Z = np.array(list(zip(DV[1].reshape(s ** 2, 1), DV[0].reshape(s ** 2, 1)))).reshape(s, s, 2)
for i in range(s):
    print(Z[i].tolist())

    % matplotlib
    notebook

    size = 256
    subgrids = 4
    unique_vectors_to_select_from = 4
    rotation_angle = 5
    v_num = subgrids + 1

    # Animation set-up
    v = generate_gradient_vectors(unique_vectors_to_select_from, v_num ** 2)
    G = generate_perlin(grid_size=size, subgrids=subgrids, vectors_matrix=v)

    fig = plt.figure()
    ax = plt.axes(xlim=(0, size), ylim=(0, size))
    im = plt.imshow(G)


    def init():
        global v, G, im
        v = rotate_vectors(v, rotation_angle)
        G = generate_perlin(grid_size=size, subgrids=subgrids, vectors_matrix=v)
        im.set_data(G)
        return [im]


    # Animation function
    def animate(i):
        global v, im, G
        v = rotate_vectors(v, rotation_angle)
        G = generate_perlin(grid_size=size, subgrids=subgrids, vectors_matrix=v)
        im.set_array(G)
        return [im]


    anim = FuncAnimation(fig, animate, init_func=init, frames=600, interval=30, blit=True)
    plt.show()