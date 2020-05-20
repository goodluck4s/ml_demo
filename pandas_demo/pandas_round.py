import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random([3, 3]),columns=['A', 'B', 'C'], index=['first', 'second', 'third'])

print(df)
print(df.round(3))
print(df.round({"A":1,"B":3}))