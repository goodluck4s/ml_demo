import numpy as np
import pandas as pd

dic={"a":["x1","x2","x3","x4"],"b":[-1,0,1,0],"c":[3,1,5,8],"d":[1,0,3,np.nan]}
df = pd.DataFrame(dic)
print(df)

df_undernorm = df.iloc[:,1:]
print(df_undernorm)
df_norm2=df_undernorm.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
print(df_norm2)

df[["b","c","d"]] = df[["b","c","d"]].apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
print(df)

print("-------------合并一下--------------")
df2 = pd.merge(df[["a"]],df_norm2,left_index=True,right_index=True,)
print(df2)
df3=df2.dropna(axis=0,how="any",inplace=False)
print(df3)
print(df2)


