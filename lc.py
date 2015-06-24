#! /usr/bin/python
import sys
from collections import Counter

def main(fp):
    c = Counter(fp)
    for item in c.most_common(5):
        print item

if __name__ == '__main__':
    main(sys.stdin)
