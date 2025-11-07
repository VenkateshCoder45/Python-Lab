import numpy as np 
import pandas as pd
df=pd.DataFrame([[1,np.nan,2],[2,3,5],[np.nan,4,6]])
print(df)
print(df.fillna(method='ffill',axis=1))