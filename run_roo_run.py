import time
import sys

import requests
import numpy as np


USER_ID = '148407016'
HOST = 'daishu.meituan.com'


def login(user_id):
    data = {
        'userId': user_id,
    }
    url = f'https://{HOST}/api/login/login'
    r = requests.post(url, json=data)
    print('login:', r.text)
    r = r.json()
    return r


def get_cars(r):
    cars = np.zeros(10240, dtype='uint')
    for car in r['player']['carList']:
        position = car['position']
        level = car['level']
        cars[position] = level
    return cars


def get_level(r):
    return r['player']['level']


def get_user_id(r):
    return r['player']['userId']


def level_up(user_id, f, t):
    assert f != t
    url = f'https://{HOST}/api/player/levelUp'
    data = {
        'f': str(f),
        't': str(t),
        'userId': user_id,
    }
    r = requests.post(url, json=data)
    print('level up:', r.text)
    r = r.json()
    return r


def buy_car(user_id, level):
    url = f'https://{HOST}/api/player/buy_car'
    data = {
        'level': str(level),
        'pos': '1',
        'userId': user_id,
    }
    r = requests.post(url, json=data)
    print('buy car:', r.text)
    r = r.json()
    return r


def run(user_id, i):
    url = f'https://{HOST}/api/player/run'
    data = {
        'i': str(i),
        'userId': user_id,
    }
    r = requests.post(url, json=data)
    print('run:', r.text)
    r = r.json()
    return r


def swap(user_id='10296083', f=5, t=12):
    url = f'https://{HOST}/api/player/swap'
    data = {
        'f': str(f),
        't': str(t),
        'userId': user_id,
    }
    r = requests.post(url, json=data)
    print('swap:', r.text)
    r = r.json()
    return r


# swap(f=1, t=32)
# swap(f=1, t=14)
# buy_car('10296083', 10)
# login(USER_ID)
# run('10296083', 4)
# run('10296083', 5)
# run('10296083', 6)
# exit()


def reward():
    url = f'https://{HOST}/api/player/level_up/reward'
    data = {
        'level': '18',
        'userId': '10296083',
        'gtoken': 't29mN20wOseodIsNm9zevM-sK355rBCmE5ZeNv6UTJP1srFYA7L_Xl6Kx--e46XY'
    }
    r = requests.post(url, json=data)
    print(r.text)
    r = r.json()
    return r


def use_power():
    url = f'https://{HOST}/api/player/use_power'
    data = {
        'userId': '10296083',
        'gtoken': 't29mN20wOseodIsNm9zevB6uBrdVpre-kKflHLS7Ysn1srFYA7L_Xl6Kx--e46XY'
    }
    r = requests.post(url, json=data)
    print(r.text)


def xx():
    url = f'https://{HOST}/api/task/meal'
    data = {
        'd': '3',
        'userId': '10296083',
        'gtoken': 't29mN20wOseodIsNm9zevF6uLB6vOl_vDSMOWxuI5jb1srFYA7L_Xl6Kx--e46XY'
    }
    r = requests.post(url, json=data)
    print(r.text)


def delete(pos):
    level_up(pos, pos)


def get():
    cars = np.zeros(10240, dtype='uint')
    r = level_up(20, 21)
    for c in r['c']:
        pos, level = c.split('_')
        pos = int(pos)
        cars[pos] = int(level)
    print(cars)
    return cars


def test():
    url = f'https://{HOST}/api/player/beat'
    data = {
        'sign': 'eac9ca0d0a50d827a7e27c548d6bb11c',
        'data': {
            'car': '[{\'level\':16,\'position\':8,\'startAt\':1},{\'level\':21,\'position\':9,\'startAt\':1},{\'level\':13,\'position\':10,\'startAt\':1},{\'level\':14,\'position\':3,\'startAt\':1}]',
            'coin': '817856512',
            'd': '209504',
            'gtoken': 't29mN20wOseodIsNm9zevLcZGJm48_eWmFCuGG90jg-CpLSicObjzKl_dg5Ww030',
            'lc': '11115',
            't': '1572256758'
        },
        'gtoken': 't29mN20wOseodIsNm9zevLcZGJm48_eWmFCuGG90jg-CpLSicObjzKl_dg5Ww030'
    }
    r = requests.post(url, json=data)
    r = r.json()
    print(r)
    return r

def sign(data):
    import hashlib
    if 'sign' in data:
        data.pop('sign')
    items = list(data.items())
    items.sort()
    data = [f'{key}={value}' for key, value in items]
    data = '&'.join(data)
    return hashlib.md5(data.encode('utf-8')).hexdigest()


login(USER_ID)
exit()


while True:
    try:
        # 更新资产
        r = login(USER_ID)
        cars = get_cars(r)
        level = get_level(r)
        level = max(1, level - 4)
        user_id = get_user_id(r)
        print('cars:', cars)
        print('level:', level)
        print('user_id:', user_id)
        # 买买买
        while True:
            r = buy_car(user_id, level)
            if r['msgId'] != 200:
                break
        # 升级
        for f in range(cars.shape[0]):
            if cars[f] == 0:
                continue
            for t in range(f + 1, cars.shape[0]):
                if cars[f] == cars[t]:
                    level_up(user_id, f, t)
                    cars[f] = 0
                    cars[t] += 1
                    break
        # 跑起来
        for i in cars.argsort()[::-1]:
            if cars[i] > 0:
                run(user_id, i)
        # 挪车位
        for i in range(1, 33):
            if cars[i] != 0:
                for j in range(33, 10240):
                    if cars[j] == 0:
                        swap(user_id, i, j)
                        cars[j] = cars[i]
                        cars[i] = 0
                        break
    except Exception as e:
        print(e)
    sys.stdout.flush()
    time.sleep(60)
