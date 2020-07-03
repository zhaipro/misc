# coding: utf-8
import os
from datetime import datetime

import pytz


def now():
    tz = pytz.FixedOffset(8 * 60)
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')


def log(msg, ofn='a.log'):
    with open(ofn, 'a') as fp:
        msg = f'{now()} {msg}'
        print(msg, file=fp)


if __name__ == '__main__':
	log('hello world')
