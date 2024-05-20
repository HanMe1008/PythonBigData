import pandas as pd
sdata = {"A boy" : 35000, "B boy" : 71000, "C boy" : 16000, "D boy" : 5000}
obj3 = pd.Series(sdata)
obj3.name = "Bigdata Expert "
obj3.index.name = "Names"
print(obj3)