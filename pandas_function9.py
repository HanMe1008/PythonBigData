import numpy as np
import pandas as pd

df3 = pd.DataFrame(np.random.randn(4, 3), columns=["b","d","e"],
                   index=["Seoul", "Incheon", "Busan", "Daegu"])
print(df3)
func = lambda x: x.max() - x.min()

#df3 = df3.apply(func, axis=0)
df3 = df3.apply(func, axis=1)
print(df3)