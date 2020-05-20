import pandas as pd
import numpy as np


dic={"a":[1,1,1,1],"b":[0,0,0,0],"c":[1,2,1,2],"d":[0,0,0,np.nan]}
a = pd.DataFrame(dic)
print(a)

print("==============替代离散值得列里的离散值=================")
a['cc']=a['c'].astype('category')
a['cc'].cat.categories=['first','two']  #即将0，1先转化为category类型再进行编码。
print(a)
