# writes the two input files in one. the freq is given. scaling is done. all periods with any zero entry in power are counted as zero
import InputReader
from pandas import Grouper
import FileWriter
import numpy as np
import pandas as pd


def hasZerosOrNan(x):
    if x.min() > 0:
        return False
    else:
        return True


def groupData(fridgeData, weatherData, freq):
    fridgeGrouped = fridgeData.groupby(Grouper(freq=freq, axis=0))
    fridgeGrouped = fridgeGrouped.agg(lambda x: np.nan if (hasZerosOrNan(x)) else x.sum())
    fridgeGrouped['power'] = fridgeGrouped['power'].round(2)

    weatherGrouped = weatherData.groupby(Grouper(freq=freq, axis=0))
    weatherGrouped = weatherGrouped.agg(lambda x: np.nan if (hasZerosOrNan(x)) else x.mean())
    return [fridgeGrouped, weatherGrouped]


def copyDataToTrain(fridgeGrouped, weatherGrouped):
    train = fridgeGrouped
    #train.index.name = indexName
    for feature in weatherGrouped.columns:
        train[feature] = weatherGrouped[feature]
        train[feature] = weatherGrouped[feature]
    return train

def blablub(filename):

    fridgeData = InputReader.createInstance(filename, "timestamp")
    fridgeData = fridgeData[1:10000]

    fridgeData.index = pd.to_datetime(fridgeData.index)

    fridgeData = fridgeData[(fridgeData.index >= "2017.07.01 00:00:00") & (fridgeData.index < "2017.08.01 00:00:00")]
    return fridgeData


def prepareData(freq):
    filenameFridgeTrain = "fridge_data"
    fridgeData=blablub(filenameFridgeTrain)
    fileNameWeatherTrain = "weather_Berlin_Tegel_per_hour"
    weather = blablub(fileNameWeatherTrain)

    #indexName = fridgeData.index.name
    #weather = InputReader.createInstance(fileNameWeatherTrain, "timestamp")
    #fridgeData.index = pd.to_datetime(fridgeData.index)
    #weather.index = pd.to_datetime(weather.index)
    #weather = weather[(weather.index >= "2017.07.01 00:00:00") & (weather.index < "2017.08.01 00:00:00")]

    [groups, groupsWeather] = groupData(fridgeData, weather, freq)
    train = copyDataToTrain(groups, groupsWeather)

    FileWriter.writePreparedInput(train, "%s%s" % ("fridgeEnergyTrain", freq))


freq = "4H"
prepareData(freq)
