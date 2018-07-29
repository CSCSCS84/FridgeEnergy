import InputReader
import matplotlib.pyplot as plt
from pandas import Grouper
import pandas as pd
import FileWriter
import seaborn as sns
#sns.set()

filenameTrain = "fridge_data4H"
train = InputReader.read(filenameTrain, "timestamp")

train.index = train.index.to_datetime()
#train.index = train.index.to_pydatetime()
#df.index.to_pydatetime()
s = train['power']


filenameWeather = "weather_Berlin_Tegel_per_hour4H"
weather = InputReader.read(filenameWeather, "timestamp")

weather.index = weather.index.to_datetime()
weather=weather[(weather.index>="2017.07.01 00:00:00") &( weather.index<"2017.08.01 00:00:00")]
train['temperature']=weather['temperature']
train['humidity']=weather['humidity']
#l=sns.relplot(data=train)
train=train[train['power']!=0]
print(type(train.index))

#scale
train['power']=(train['power']-train['power'].min())/(train['power'].max()-train['power'].min())
train['temperature']=(train['temperature']-train['temperature'].min())/(train['temperature'].max()-train['temperature'].min())
train['humidity']=(train['humidity']-train['humidity'].min())/(train['humidity'].max()-train['humidity'].min())

#fig, axs = plt.subplots(ncols=3)
#sns.tsplot(data= train['temperature'],time = train.index)
#sns.tsplot(data=weather['temperature'], time=weather.index)
plt.plot(train)
plt.show()
