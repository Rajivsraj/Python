import pandas as pd

s = pd.Series([10, 20, 30, 40])

s[4] = 50
print(s)
print(len(s))