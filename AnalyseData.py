import InputReader
from matplotlib import pyplot
from pandas import Grouper
import pandas as pd
import OutputWriter
import numpy as np

filenameTrain = "fridge_data"
train = InputReader.createInstance(filenameTrain, "timestamp")
train['power'].replace(0,np.nan)

#train = train[1:100000]

# print(train)
#print(train.isnull().sum())
#print(train.info())

#s = train['power']
#print(type(s))

# s.plot()
# pyplot.show()

train.index = train.index.to_datetime()
freq="4H"

groups = train.groupby(Grouper(freq=freq, axis=0)).sum()


OutputWriter.writeToFile(groups,"%s%s" %(filenameTrain,freq))
print(type(groups))

print(groups)
#years = pd.DataFrame()
#for name, group in groups:
#    years[name.year] = group.values
#s=groups['power']
#s.plot()
#pyplot.show()