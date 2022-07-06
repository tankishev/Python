import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial as Poly


def interpolate_polynomial(points, degree, min_x, max_x, title=None, add_func=None):
    """
    Interpolates a polynomial of the specified degree through the given points and plots it
    points - a list of points (x, y) to plot
    degree - the polynomial degree
    min_x, max_x - range of x values used to plot the interpolating polynomial
    """
    pts = np.array(points)
    x = pts[:, 0]
    y = pts[:, 1]
    p = Poly.fit(x, y, degree)
    p = p.convert(domain=[min_x, max_x])
    p_plot = p.linspace(1000)
    plt.plot(p_plot[0], p_plot[1], c="green")

    if add_func:
        v_y = np.vectorize(add_func)
        x2 = np.linspace(min_x, max_x, 1000)
        y2 = v_y(x2)
        plt.plot(x2, y2, c="blue")

    if title:
        plt.title(title)
    else:
        plt.title(f'Polynomial of degree {degree}')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.scatter(x, y)
    plt.show()


points = np.array([(0, 0), (1, 0.8), (2, 0.9), (3, 0.1), (4, -0.8), (5, -1.0)])
interpolate_polynomial(points, len(points) - 1, -1, 6, add_func=lambda x: 1/(1+x**2))