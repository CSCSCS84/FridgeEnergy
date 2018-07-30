# writes the two input files in one. the freq is given. scaling is done. all periods with any zero entry in power are counted as zero
import InputReader
from pandas import Grouper
import FileWriter
import numpy as np
import pandas as pd
import Constants
from datetime import timedelta


def hasZerosOrNan(x):
    if x.min() > 0:
        return False
    else:
        return True


def groupFridgeData(fridgeData, freq):
    fridgeGrouped = fridgeData.groupby(Grouper(freq=freq, axis=0))
    intervalLength = float(freq.replace("s", ""))
    fridgeGrouped = fridgeGrouped.agg(lambda x: np.nan if (hasZerosOrNan(x)) else x.mean() * intervalLength)
    fridgeGrouped = fridgeGrouped.round(2)
    print(fridgeGrouped)
    fridgeGrouped.rename({'power': 'energy'}, axis=1, inplace=True)
    return fridgeGrouped


def groupWeatherData(weatherData, freq):
    weatherGrouped = weatherData.groupby(Grouper(freq=freq, axis=0))
    weatherGrouped = weatherGrouped.agg(lambda x: np.nan if (hasZerosOrNan(x)) else x.mean())
    weatherGrouped = weatherGrouped.round(2)
    return weatherGrouped


def joinData(fridgeGrouped, weatherGrouped):
    train = fridgeGrouped
    for feature in weatherGrouped.columns:
        train[feature] = weatherGrouped[feature]
        train[feature] = weatherGrouped[feature]
    return train


def readDataFromRange(filename):
    data = InputReader.read(filename, Constants.indexName)
    data.index = pd.to_datetime(data.index)
    data = data[(data.index >= Constants.startDate) & (data.index <= Constants.endDate)]
    return data


def addDummyRow(weatherData):
    temperature = weatherData['temperature']
    temperature.index = temperature.index - timedelta(seconds=1)
    humidity = weatherData['humidity']
    humidity.index = humidity.index - timedelta(seconds=1)
    weatherData2 = pd.DataFrame()
    weatherData2['temperature'] = temperature
    weatherData2['humidity'] = humidity
    weatherData2 = weatherData2.drop(weatherData2.index[0])
    weatherData = weatherData.append(weatherData2)
    return weatherData


def prepareData(freq):
    fridgeData = readDataFromRange(Constants.filenameFridgeTrain)
    weatherData = readDataFromRange(Constants.fileNameWeatherTrain)
    fridgeData.index = pd.to_datetime(fridgeData.index)
    weatherData.index = pd.to_datetime(weatherData.index)
    weatherData = addDummyRow(weatherData)
    fridgeGrouped = groupFridgeData(fridgeData, freq)
    weatherGrouped = groupWeatherData(weatherData, freq)
    train = joinData(fridgeGrouped, weatherGrouped)
    return train


def savePreparedInput(train):
    FileWriter.writePreparedInput(train, "%s%s" % (Constants.fileNameTrain, freq))


freq = "14400s"
train = prepareData(freq)
savePreparedInput(train)
