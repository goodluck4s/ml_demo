import numpy as np
import pandas as pd

dic={"a":[1,1,1,1],"b":[0,0,0,0],"c":[3,1,5,8],"d":[0,0,0,np.nan]}
df = pd.DataFrame(dic)
print(df)

print("____________________")
df2=df.sample(n=2,axis=0) #按条目数
print(df2)
df2=df.sample(frac=0.25,axis=0)  #按比例
print(df2)
print("____________________")
print(df)
