# coding: utf-8
import random
import copy
from collections import defaultdict
import cPickle as pickle

import numpy as np


def compute_strategy(regret_sum):
    strategy = np.maximum(regret_sum, 0)
    normalizing_sum = strategy.sum()
    if normalizing_sum > 0:
        return strategy / normalizing_sum
    else:
        return np.ones_like(regret_sum) / regret_sum.size


def training(N, A, u, times=10000):     # NOQA
    u = np.vectorize(u, otypes=[np.float])
    regret_sum = np.zeros(A)
    strategy_sum = np.zeros(A)
    opp_strategy = np.array([1. / 3, 1. / 3, 1. / 3])
    for _ in xrange(times):
        strategy = compute_strategy(regret_sum)
        strategy_sum += strategy
        action = np.random.choice(np.arange(A), 1, p=strategy)
        action = action[0]
        opp_action = np.random.choice(np.arange(A), 1, p=opp_strategy)
        opp_action = opp_action[0]
        regret = u(np.arange(A), opp_action) - u(action, opp_action)
        regret_sum += regret
    return strategy_sum / times


def u(a1, a2):
    d = a1 - a2
    if d == 2:
        d = -1
    elif d == -2:
        d = 1
    return d


# print training(2, 3, u, times=10000)


class History:
    def __init__(self):
        self.h = []

    def __add__(self, a):
        self.h.append(a)


class XXX:
    N = 2

    PASS = 0    # NOQA
    BET = 1     # NOQA
    CHECK = 2   # NOQA

    class History:
        def __init__(self, N):  # NOQA
            self.poker = random.randint(1, 13)
            self.cur_player = 0
            self.cur_value = 0

            self.players = [0] * N
            self.players[0] = 1

            self.N = N
            self.passed_number = 1

        def __add__(self, a):
            h = copy.deepcopy(self)
            h.cur_value += a
            if a == 0:
                h.players[h.cur_player] = 1
                h.passed_number += 1
            h.cur_player = (h.cur_player + 1) % h.N
            return h

        def is_terminal(self):
            return self.cur_value >= self.poker

    def __init__(self, N):  # NOQA
        self.N = N
        self.sigma = {}
        self.regret = defaultdict(float)
        self.strategy_sum = defaultdict(float)

    @classmethod
    def A(cls, I):      # NOQA
        if I[4]:
            return 1, 2, 3
        else:
            return 0, 1, 2, 3

    @classmethod
    def I(cls, i, h):   # NOQA
        poker = -1
        if i == 0:
            poker = h.poker
        return poker, h.cur_value, h.N, h.passed_number, h.players[i]

    @classmethod
    def P(cls, h):          # NOQA
        return h.cur_player

    @staticmethod
    def u(i, h):
        loser = (h.cur_player + h.N - 1) % h.N
        return int(loser != i)

    def _CFR(self, h, i, pi):    # NOQA
        if h.is_terminal():
            return self.u(i, h)
        v = 0.0
        p = self.P(h)
        I = self.I(p, h)       # NOQA
        pi_p = pi[p]
        v_ = {}
        A = self.A(I)
        for a in A:
            self.sigma.setdefault((I, a), 1.0 / len(A))
            pi[p] = pi_p * self.sigma[I, a]
            v_[a] = self._CFR(h + a, i, pi)
            v += self.sigma[I, a] * v_[a]
        pi[p] = pi_p

        if self.P(h) == i:
            normal = 0.0
            for a in A:
                self.regret[I, a] += self.pi_i(pi, i) * (v_[a] - v)
                if self.regret[I, a] > 0:
                    normal += self.regret[I, a]
                self.strategy_sum[I, a] += pi[i] * self.sigma[I, a]
            for a in A:
                if normal > 0:
                    self.sigma[I, a] = max(self.regret[I, a], 0) / normal
                else:
                    self.sigma[I, a] = 1.0 / len(A)

        return v

    def CFR(self, times=1000):  # NOQA
        pi = [1.0] * self.N
        for t in xrange(times):
            for i in xrange(self.N):
                h = XXX.History(self.N)
                self._CFR(h, i, pi)

    @staticmethod
    def pi_i(pi, i):    # 反事实到达概率
        result = 1.0
        pi_i = pi[i]
        pi[i] = 1.0
        for p in pi:
            result *= p
        pi[i] = pi_i
        return result

    @staticmethod
    def get_average_strategy(strategy_sum):
        normal = defaultdict(float)
        strategy = {}
        for (I, a), p in strategy_sum.iteritems():
            normal[I] += p
        for (I, a), p in strategy_sum.iteritems():
            strategy[I, a] = p / normal[I]
        return strategy

    def play(self, i, strategy=None):
        h = XXX.History(self.N)
        if strategy is None:
            strategy = self.get_average_strategy(self.strategy_sum)
        for x in xrange(100):
            x %= self.N
            if h.is_terminal():
                print 'game over, poker:', h.poker, 'u:', self.u(i, h)
                break
            I = self.I(x, h)
            if self.P(h) == i:
                a = raw_input('I: %r player: %d action: ' % (I, x))
                a = int(a)
            else:
                a = self.choice(strategy, I)
                print 'I:', I, 'player:', x, 'action:', a
            h = h + a

    @classmethod
    def choice(cls, strategy, I):   # NOQA
        A = cls.A(I)                # NOQA
        p = [strategy[I, a] for a in A]
        a = np.random.choice(A, p=p)
        return a

'''
x = XXX(5)
x.CFR(100)
strategy = XXX.get_average_strategy(x.strategy_sum)
for k, p in strategy.iteritems():
    if p > 0.1:
        print k, p
pickle.dump(strategy, open('strategy.pick', 'w'))
'''

strategy = pickle.load(open('strategy.pick'))
XXX(5).play(0, strategy)
