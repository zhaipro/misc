#! python
import pandas as pd
import sys


print pd.Series(map(int, sys.stdin)).describe()
