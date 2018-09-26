#! env python3
# coding: utf-8
import argparse
import csv
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='list', default=0, help='default: 0', type=int)
args = parser.parse_args()

try:
    for row in csv.reader(sys.stdin):
        row = row[args.list]
        print(row)
except BrokenPipeError:
    # https://stackoverrun.com/cn/q/7325723
    sys.stderr.close()
