# coding: utf-8
import numpy as np


class RandomValue:

    def sample(self):
        raise NotImplementedError

    @staticmethod
    def _check_type(other):
        if isinstance(other, (int, float)):
            other = Constant(other)
        return other

    def __add__(self, other):
        other = self._check_type(other)
        return AddNode(self, other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self._check_type(other)
        return SubNode(self, other)

    def __rsub__(self, other):
        other = self._check_type(other)
        return other - self

    def __lt__(self, other):
        return LtNode(self, other)


class Normal(RandomValue):

    def __init__(self, mu=0.0, sigma=1.0):
        self.mu = mu
        self.sigma = sigma

    def sample(self):
        return np.random.normal(self.mu, self.sigma)


class Constant(RandomValue):

    def __init__(self, c):
        self.c = c

    def sample(self):
        return self.c


class Node(RandomValue):

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


class AddNode(Node):

    def sample(self):
        return self.v1.sample() + self.v2.sample()


class SubNode(Node):

    def sample(self):
        return self.v1.sample() - self.v2.sample()


class MultNode(Node):

    def sample(self):
        return self.v1.sample() * self.v2.sample()


class DivNode(Node):

    def sample(self):
        return self.v1.sample / self.v2.sample()


class LtNode(Node):

    def sample(self):
        return int(self.v1.sample() < self.v2.sample())


def E(value, times=10000):    # NOQA
    s = 0.0
    for _ in xrange(times):
        s += value.sample()
    return s / times

if __name__ == '__main__':
    X = Normal()
    print X.sample()
    print E(X)

    Y = 3 + X - 1
    print Y.sample()
    print E(Y)

    Z = X < Y
    print Z.sample()

    X = 1200
    for _ in xrange(14):
        X = X + Normal(400, 900)
    Y = 0
    for _ in xrange(15):
        Y = Y + Normal(400, 900)
    print E(Y < X, times=50000)
