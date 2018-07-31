# Creates some plots for the problem
# Note: Some of the files might not be created. Use PrepareInput to create a file with a given frequence
import InputReader
import matplotlib.pyplot as plt
import pandas as pd
import Scaler
import Constants
from datetime import timedelta
from datetime import datetime


def create24HPlot():
    filenameTrain = "fridgeEnergyTrain_86400s"
    train = InputReader.read(filenameTrain, "timestamp")
    train.index = pd.to_datetime(train.index)
    train_scaled = Scaler.minMaxScale(train)
    plt.plot(train_scaled)
    plt.show()


def plotDifferentFrequences():
    frequences = ["3600s", "14400s", "28800s", "86400s"]
    for freq in frequences:
        train = InputReader.read("fridgeEnergyTrain_%s" % (freq), "timestamp")
        train.index = pd.to_datetime(train.index)
        train_scaled = Scaler.minMaxScale(train)
        plt.plot(train_scaled)
        plt.title("Frequence %s" % (freq))
        plt.show()


def calcCorrelation():
    frequences = ["3600s", "14400s", "28800s", "86400s"]
    for freq in frequences:
        print("Correlation for frequence %s:" % (freq))
        train = InputReader.read("fridgeEnergyTrain_%s" % (freq), "timestamp")
        correlation = train.corr().round(2)
        print(correlation)
        print()


def plotEachDay():
    filenameTrain = "fridgeEnergyTrain_14400s"
    train = InputReader.read(filenameTrain, "timestamp")
    train.index = pd.to_datetime(train.index)
    startDate = datetime.strptime(Constants.startDate, "%Y-%m-%d %H:%M:%S")
    endDateOfTrain = datetime.strptime(Constants.endDate, "%Y-%m-%d %H:%M:%S")

    oneDay = timedelta(days=1)
    endDate = startDate + oneDay
    while startDate < endDateOfTrain:
        trainDay = train[(train.index >= startDate) & (train.index <= endDate)]
        trainDay = Scaler.minMaxScale(trainDay)
        plt.plot(trainDay)
        plt.title(startDate)
        plt.show()
        startDate = startDate + oneDay
        endDate = endDate + oneDay


#create24HPlot()
#plotDifferentFrequences()
#calcCorrelation()
#plotEachDay()
