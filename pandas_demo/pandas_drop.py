import numpy as np
import pandas as pd

dic={"a":[1,1,1,1],"b":[0,0,0,0],"c":[3,1,5,8],"d":[0,0,0,np.nan]}
df = pd.DataFrame(dic)
print(df)

print("==================分割线==============")
df_part = df.drop(labels=["a","b"],axis =1,inplace=False) # 维度1删的是列
print(df_part)
df_part.drop([0,3],inplace=True) #默认是维度0  删的是行
print(df_part)


print("==================分割线= dropNan=============")
dic={"a":[1,1,1,1],"b":[0,0,0,0],"c":[3,1,5,8],"d":[0,0,0,np.nan]}
df = pd.DataFrame(dic)
print(df)
df2=df.dropna(axis=0,how="any",inplace=False)
print(df2)