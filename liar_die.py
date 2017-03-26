# coding: utf-8
import numpy as np
import random


DOUBT = 0
ACCEPT = 1


def normalizing(vector):
    normalizing_sum = vector.sum()
    if normalizing_sum > 0:
        vector /= normalizing_sum
    else:
        vector.fill(1.0 / vector.size)
    return vector


def get_strategy(regret_sum):
    strategy = np.maximum(regret_sum, 0)
    return normalizing(strategy)


def get_average_strategy(strategy_sum):
    # 该方法会将结果写回数组strategy_sum
    return normalizing(strategy_sum)


class Node:

    def __init__(self, num_actions):
        self.regret_sum = np.zeros(num_actions)
        self.strategy = np.zeros(num_actions)
        self.strategy_sum = np.zeros(num_actions)

if __name__ == '__main__':
    random.randint()
