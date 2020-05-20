import numpy as np
import pandas as pd

dic={"a":[1,2,3,3],"b":[4,3,2,1],"c":[3,1,5,8],"d":[0,0,0,np.nan]}
df = pd.DataFrame(dic)
print(df)

print("++++++++++++++排序++++++++++++++++")
a=df.sort_values(by=["a","b"] , ascending=False,inplace=False)
print(a)