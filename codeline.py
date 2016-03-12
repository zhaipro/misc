# coding: utf-8

import sys
import os


l = []
for path, dirs, fns in os.walk('.'):
    for fn in fns:
        if fn.endswith('.py'):
            fn = os.path.join(path, fn)
            fp = open(fn)
            l.append((len(fp.readlines()), fn))

l.sort(reverse=True)
for lines, path in l:
    print lines, path
