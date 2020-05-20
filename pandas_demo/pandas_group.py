import pandas as pd
import numpy as np


df = pd.DataFrame({'A': ['a', 'b', 'a', 'c', 'a', 'c', 'b', 'c'],
                  'B': [2, 8, 1, 4, 3, 2, 5, 9],
                     'C': [102, 98, 107, 104, 115, 87, 92, 123],
                   "D":[1,2,3,4,5,6,7,8]})
print(df)

print("=================分割线===groupby数据类型与遍历================")
g = df.groupby("A")
print(type(g))
for a,b in g:
    print(type(a),a)
    print(type(b))
    print(b)






print("==============通过组的名字拿到组===分割线===================")
print(g.get_group("a"))









print("==============groupBy  一般聚合===================")
# 1按A列分组（groupby），获取其他列的均值
print(df.groupby('A').std())
# 2按多列进行分组（groupby）
print(df.groupby(['A','B']).size())   #count()不算NAN 但是size会算
# 3按A列分组 分别计算B C两列的均值
print(df.groupby('A')[["B","C"]].mean())










print("==============groupBy  agg聚合===================")
# 1按A列分组 不同列用不同的聚合函数
g = df.groupby('A')
print(g.agg({"B":"mean","C":"count","D":np.std}))
print(g.agg({"B":["mean",np.max],"C":"count","D":[np.std,np.var]}))  # std=标准差  var=方差









print("==============groupBy  apply聚合===================")
# 1按A列分组 不同列用不同的聚合函数
print(df)
g = df.groupby('A')
print(g.apply(np.std))  #同 df.groupby('A').std()
print(g.apply(lambda x: (x['C']-x['B']).mean())) #用lambda





