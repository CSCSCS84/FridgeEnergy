import InputReader
import matplotlib.pyplot as plt
import pandas as pd
import MinMaxScaler
import Constants
from datetime import timedelta
from datetime import datetime

def plot24Hour():
    filenameTrain = "fridgeEnergyTrain24H"
    train = InputReader.read(filenameTrain, "timestamp")
    train.index = pd.to_datetime(train.index)

    train_scaled = MinMaxScaler.scale(train)
    f, ax = plt.subplots(1, 1)
    ax.legend()
    plt.plot(train_scaled)
    plt.show()

def plotDifferentFrequences():
    frequences = ["3600s", "14400s", "28800s", "86400s"]
    for freq in frequences:
        train = InputReader.read("fridgeEnergyTrain%s" % (freq), "timestamp")
        train.index = pd.to_datetime(train.index)
        train_scaled = MinMaxScaler.scale(train)
        plt.plot(train_scaled)
        plt.title(freq)
        plt.show()

def calcCorrelation():
    frequences = ["3600s","14400s","28800s","86400s"]
    for freq in frequences:
        print("Correlation for frequence %s:" %(freq))
        train = InputReader.read("fridgeEnergyTrain%s" % (freq), "timestamp")
        correlation = train.corr().round(2)
        print(correlation)
        print()


def plotEachDay():
    filenameTrain = "fridgeEnergyTrain14400s"
    train = InputReader.read(filenameTrain, "timestamp")
    train.index = pd.to_datetime(train.index)
    print(train)
    startDate=datetime.strptime(Constants.startDate,"%Y-%m-%d %H:%M:%S")
    endData1=datetime.strptime(Constants.endDate,"%Y-%m-%d %H:%M:%S")
    print(startDate)

    day=timedelta(days=1)
    endDate=startDate+day
    print(endDate)
    while startDate<endData1:

        trainDay=train[(train.index>=startDate) & (train.index <=endDate)]
        trainDay=MinMaxScaler.scale(trainDay)
        plt.plot(trainDay)
        plt.title(startDate)
        plt.show()
        startDate=startDate+day
        endDate=endDate+day




#plotEachDay()
plotEachDay()
#plotDifferentFrequences()
calcCorrelation()
#plot24Hour()



