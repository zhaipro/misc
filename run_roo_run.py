import time
import sys

import requests
import numpy as np


user_id = '10296083'
host = 'daishu.meituan.com'


def level_up(f, t):
    assert f != t
    url = f'https://{host}/api/player/levelUp'
    data = {
        'f': str(f),
        't': str(t),
        'userId': user_id,
    }
    r = requests.post(url, json=data)
    r = r.json()
    print('level up', r)
    return r
    # {'cmd': 200, 'levelUpReward': None, 'dropReward': None, 'bank': 328557, 'coin':0, 'c': None}


def login():
    data = {
        'userId': '148407016',
        'uuid': '176C6F0D97A074702593F32B197DD18049F36DD633FC25D5A2D5621CB2D4F641',
        'token': 'ItL5msfUAUkFGNK8C-WoKQjIZFQGAAAAUwkAAHPJ2-BZaj6l3zXs7RV-MDfvty4zGEqQHOTP0ck8geexf1pX6dCoPLVA6iiJtSz8-Q',
        'fingerprint': 'i2HKpOmsirDPavelVfQBZN828UKVzEtaCwTT6xrFJPN1dVITZo42xjjeNLfLm/leEYLC3YHlXbK8w+pb4+CHWP7E1lwEva7f+0dUECVASqaHXkVdzeWNgORQSraVqSwp68I6BzP22Gst8swGqBcT3kdnCwFZC1ROzUIaiORf07zp/mozSS7nH5uLtCV9IoVOscVSrpU3hjf6ANAIyWoGyHKb2iPkTirHVEgyyOo9gl5DBXWFuVdq/XvE3Aqo01U5L2DC3ooA0GAvtWFZgyfPaWzL93PL8TNqp3Ha8+D1i3h/QAY+gdyluXV4D7/fRFRGsaNhFPWzneQ4hRgAEIq/smeK8nSr1aaueWramRfyQpD10C0gITwZ7pN/0uuCmIiIBKgIrQgo+LQCvsJt7MmnGRpJ+1opm05ZuhS4xAKVDB8UX+xK6EcrwA5V/Utzb7CJunXs+RpOGdDpcBUrv9yBfnZZpeOp3msHXdaNg8OiHdSL86nQ6GHlPINh4MabisvNz2V0llGoQwjxZiiP/PpZBTgvzWr85ZA81YJh8NtvgXwC/ieucVpgNV+naHEgwMw4HjhKhaftsW7tjyvnljoHINDhrOQCgQrB/La/K2ItqNP2Ap7ACUvcx5Mu8OFmlFDZ0ccaPjme2J5SBUP/IPRjBhjtimXpr9C73Az2zGjsrQ5BZLkxJmkII9kxZa3RHV6wgtpp84wMsxnQwyX6J1jXRgkBF4fGrbrLJ7a6d2iKCqCiVIba+ghveFidzfg/juma3b7CiXPd/NruB9BQKwCKXOzsExSU7gBRN/SyXtBce24n+bj4o7Obbmz9htujvjG7VoWQ545OdF1anntTFfzG9FcM4KlL2Vt3iToYN3teMEdD+9sod2aCeaI2aRmNhpCMff0bZhm/O0zSVCiSeLRF42/5FmTXrCSX4HiQzECYrvS7Yvzqypq5aRzunBL7jvaddlixek7OjNIukrRyC3UbMNoVS0IQm0Jz++xtspxq6nMt58qq9xm3/nxPxpAMTdFTNzD3YNhnwKyNZE0NofD8dfg0c1Ne7dO3FuNdU3NwEKNu7TCt41n5N8/SdKLRYMoCawRjsinKA/pGc9is+JDV0qIb7fwdMK0cmepxylW7wrIhl4C02Aj1aJ9smgqGkjAoZLNDcfvsTm1tDLFqnENKQykLWUeH8nUsQ+2tMgfbhM+0xN+cG57bCTwRrq0Azu/wCC/9Kik00I2DJO42EiOn9zpg817E4J9elBzv3r9PobPYUJl8i2oDGpwtC7NHbnzpLlBE055p483tYjbgOLPVeWzneCIT+8nEINsNeCKmrWUWEkgoqDOvT8gn8opcJFlcCbGxs6RebejE+ZJhK87HpaAOjGkFdMRjLgSrdKhufLx0O0A90GbGapQAjZVs4bnqafvA/bgCd/u3Rw5ods2KUwIWHy+VLX6S+KnzxaI6NqgNf5fXGTLKO8pv7Ic7Y8JN',
        'gameType': '1'
    }
    url = f'https://{host}/api/login/login'
    r = requests.post(url, json=data)
    print(r.json())


def buy_car(level):
    url = f'https://{host}/api/player/buy_car'
    data = {
        'level': str(level),
        'pos': '1',
        'userId': user_id,
    }
    r = requests.post(url, json=data)
    r = r.json()
    print('buy car:', r)
    return r
    # {'msgId': 200, 'reqNo': 0, 'buyCar': {'level': 2, 'position': 8, 'startAt': 0},'num': 28, 'bank': 328350, 'b': None, 'gtoken': None}


def run(i):
    url = f'https://{host}/api/player/run'
    data = {
        'i': str(i),
        'userId': user_id,
    }
    r = requests.post(url, json=data)
    r = r.json()
    print(r)
    return r


def delete(pos):
    level_up(pos, pos)


def get():
    cars = np.zeros(32, dtype='uint')
    r = level_up(20, 21)
    for c in r['c']:
        pos, level = c.split('_')
        pos = int(pos)
        cars[pos] = int(level)
    print(cars)
    return cars


def test():
    url = f'https://{host}/api/player/beat'
    data = {
        'sign': 'e4b7904105076bf3445db6f99caf25d8',
        'data': {
            'car': '[{\'level\':8,\'position\':8,\'startAt\':1},{\'level\':5,\'position\':1,\'startAt\':1},{\'level\':9,\'position\':9,\'startAt\':1},{\'level\':6,\'position\':2,\'startAt\':1},{\'level\':2,\'position\':3,\'startAt\':1},{\'level\':1,\'position\':4,\'startAt\':1},{\'level\':1,\'position\':5,\'startAt\':0},{\'level\':1,\'position\':6,\'startAt\':0}]',
            'coin': '27624',
            'd': user_id,
            'gtoken': 't29mN20wOseodIsNm9zevA4ZZOOVf6WREUPLe-pQV6j1srFYA7L_Xl6Kx--e46XY',
            'lc': '20570',
            't': str(int(time.time()))
        },
        'gtoken': 't29mN20wOseodIsNm9zevA4ZZOOVf6WREUPLe-pQV6j1srFYA7L_Xl6Kx--e46XY'
    }
    r = requests.post(url, json=data)
    r = r.json()
    print(r)
    return r


# 默认前6量在跑单
# login()
# level_up(4, 4)
# buy_car(4)
# get()
# run(1)
while True:
    try:
        # 买买买
        while True:
            r = buy_car(6)
            if r['msgId'] != 200:
                break
        # 升级
        cars = get()
        for f in range(cars.shape[0]):
            if cars[f] == 0:
                continue
            for t in range(f + 1, cars.shape[0]):
                if cars[f] == cars[t]:
                    level_up(f, t)
                    cars[f] = 0
                    cars[t] += 1
                    break
        # 跑起来
        for i in cars.argsort()[::-1]:
            if cars[i] > 0:
                run(i)
        sys.stdout.flush()
    except:
        pass
    time.sleep(60)
