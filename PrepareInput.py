# writes the two input files in one. the freq is given. scaling is done. all periods with any zero entry in power are counted as zero
import InputReader
from pandas import Grouper
import FileWriter
import numpy as np
import pandas as pd
import Constants


def hasZerosOrNan(x):
    if x.min() > 0:
        return False
    else:
        return True


def groupFridgeData(fridgeData, freq):
    fridgeGrouped = fridgeData.groupby(Grouper(freq=freq, axis=0))
    fridgeGrouped = fridgeGrouped.agg(lambda x: np.nan if (hasZerosOrNan(x)) else x.sum())
    fridgeGrouped = fridgeGrouped.round(2)
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


def prepareData(freq):
    fridgeData = readDataFromRange(Constants.filenameFridgeTrain)
    weatherData = readDataFromRange(Constants.fileNameWeatherTrain)
    fridgeData.index = pd.to_datetime(fridgeData.index)
    weatherData.index = pd.to_datetime(weatherData.index)
    fridgeGrouped = groupFridgeData(fridgeData, freq)
    weatherGrouped = groupWeatherData(weatherData, freq)
    train = joinData(fridgeGrouped, weatherGrouped)
    return train


def savePreparedInput(train):
    FileWriter.writePreparedInput(train, "%s%s" % (Constants.fileNameTrain, freq))


freq = "4H"
train = prepareData(freq)
savePreparedInput(train)
