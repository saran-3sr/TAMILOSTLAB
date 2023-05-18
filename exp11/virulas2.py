import pandas as pd
import numpy as np
import math
sample=[3,4,7,8,10,12,15,16,18,20]
mean_panda=pd.Series(sample).mean()
mean_math=sum(sample)
print(mean_math)
print(mean_panda)