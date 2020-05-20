import numpy as np
import pandas as pd

dic={"a":[1,1,1,1],"b":[0,0,0,0],"c":[3,1,5,8],"d":[0,0,0,np.nan]}
df = pd.DataFrame(dic)
print(df)

print("==============选择loc iloc(选行)====分割线=================")
# 通过标签 列的标签  当然可以通过选择后来进行赋值  下同
print(df.loc[0:1,["a","c"]])
print(df.loc[[1,3],["a","c"]])
# 通过坐标 可以切片
print(df.iloc[0:1,1:2])
df_part1 = df.iloc[[1,3],2:3] #按 1,3行  第2到3列拿数 既可以按标签也能按索引
print(df_part1)

print("==============loc条件表达式 ==分割线=================")
print(df)
df_part1 = df.loc[:,~((df==0).all())] #选择非(全列为1或全列有任意一个0)的全部数据
print(df_part1)
df_part1 = df.loc[:,~((df==3).any()&(df==8).any())] #选择非(全列有任意一个3并且有任意一个8)的全部数据
print(df_part1)
df_part1 = df.loc[:,(df==1).all()|(df==0).all()] #选择(全列为1或全列为0)的全部数据
print(df_part1)



