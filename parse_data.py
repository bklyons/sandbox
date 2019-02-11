import os
import pandas as pd

DATA_DIR = 'data'
files = os.listdir(DATA_DIR)
dataset = pd.DataFrame()
for filename in files:
    print(filename)
    fullpath = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(fullpath, delimiter=',', parse_dates=['Date'], index_col='Date')
    if dataset.empty:
        dataset = df
    else:
        dataset = pd.merge(dataset, df, left_index=True, right_index=True, how= 'inner')
dataset = dataset.fillna(0)
ds2 = dataset.loc['1998-12-23':]
ds2.to_csv(os.path.join(DATA_DIR, 'merged.csv'))
