import numpy as np
import pandas as pd

dic={"a":[1,1,1,1],"b":[0,0,0,0],"c":[3,1,5,8],"d":[0,0,0,np.nan]}
df = pd.DataFrame(dic)
print(df)

print("==============缺失值填充==替换值==分割线=================")
df_part1 = df.fillna(0,inplace=False) #缺失值填充
print(df_part1)
df_part1 = df.replace(8,0,inplace=False) #值替换 这里是从8->0
print(df_part1)

