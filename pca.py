import sklearn.preprocessing as pre
import sklearn.utils.extmath as ex
import pandas as pd
import numpy as np

df = pd.read_csv('data/merged.csv', delimiter=',', parse_dates=['Date'], index_col='Date')
headers = list(df)
N = len(headers)
np_array = np.array(df)
scaler = pre.StandardScaler()
scaler.fit(np_array)
whitened = scaler.transform(np_array)
U, sigma, VT = ex.randomized_svd(np_array, N)

