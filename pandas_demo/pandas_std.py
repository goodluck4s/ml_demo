import pandas as pd
import numpy  as np

dic={"a":[1,1,1,1],"b":[np.nan,np.nan,np.nan,np.nan],"c":[1,1,1,5],"d":[1,2,0,np.nan]}
a = pd.DataFrame(dic)
print(a)
print(a.describe().loc[["count","mean","std"]])
print("-------pandas 在算std时需要一个参数 否则算的不对  另外 pandas describe中的std算的不对---------")
print(a.std(ddof=0)) #pandas 在计算std和countMean的时候 是不算nan的  再describe中也是怎么算的
b=a.describe().loc[["count","mean","std"]]
b.loc["std"] = a.std(ddof=0)
print(b)
print("count",a.count())
print("mean",a.mean())

