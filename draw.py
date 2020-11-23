import matplotlib.pyplot as plt
import numpy as np


def draw(f, start, stop, num=50):
    x = np.linspace(start, stop, num=num)
    y = f(x)
    plt.title("f")
    plt.plot(x, y)
    plt.show()


def softplus(x):
    return np.log(1 + np.exp(x))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    draw(sigmoid, -5, 5)
