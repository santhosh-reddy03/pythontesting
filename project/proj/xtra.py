import numpy as np
import pandas as pd


df = pd.DataFrame([1,2,3], columns=['a'])
a = df
print(id(a))
print(id(df))
x = np.array([1,"a",3])
print(x.shape)

