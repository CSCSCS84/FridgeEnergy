# Prepares the input. Groups the data to the given frequence. The two input files are saved in one new file with the name
# fridgeEnergyTrain%s with s=frequence. From the given power values the energy in the period is calculated. The temperature
# and humidity are the mean values in the period.
import InputReader
from pandas import Grouper
import FileWriter
import numpy as np
import pandas as pd
import Constants
from datetime import timedelta


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


# not used yet
def addOfficeIsOpenRow(data):
    officeIsOpen = pd.DataFrame(data.index)
    officeIsOpen = data.index.map(lambda s: 1 if s == "2017-07-01" else 0)
    data['officeIsOpen'] = officeIsOpen
    return data


# dummy row for mean calculation of temperature and humidity
def addDummyRow(weatherData):
    temperature = weatherData['temperature']
    temperature.index = temperature.index - timedelta(seconds=1)
    humidity = weatherData['humidity']
    humidity.index = humidity.index - timedelta(seconds=1)

    weatherDataDummy = pd.DataFrame()
    weatherDataDummy['temperature'] = temperature
    weatherDataDummy['humidity'] = humidity
    weatherDataDummy = weatherDataDummy.drop(weatherDataDummy.index[0])
    weatherData = weatherData.append(weatherDataDummy)
    return weatherData


def savePreparedInput(train, freq):
    FileWriter.writePreparedInput(train, "%s_%s" % (Constants.fileNameTrain, freq))

def run():
    frequence = "14400s"
    train = prepareData(frequence)
    savePreparedInput(train, frequence)

run()
