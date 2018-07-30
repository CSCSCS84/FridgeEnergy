import InputReader
import matplotlib.pyplot as plt
import pandas as pd
import MinMaxScaler
import seaborn as sns
import Constants
from datetime import timedelta
from datetime import datetime

def plot24Hour():
    filenameTrain = "fridgeEnergyTrain24H"
    train = InputReader.read(filenameTrain, "timestamp")
    train.index = pd.to_datetime(train.index)

    train_scaled = MinMaxScaler.scale(train)
    f, ax = plt.subplots(1, 1)
    # ax.plot_date(train_scaled.energy, train_scaled["energy"], color="blue", label="A", linestyle="-")
    ax.legend()
    plt.plot(train_scaled)
    plt.show()

def calcCorrelation():

    filenameTrain = "fridgeEnergyTrain8H"
    train = InputReader.read(filenameTrain, "timestamp")
    correlation = train.corr().round(2)
    print(correlation)


def plotEachDay():
    filenameTrain = "fridgeEnergyTrain4H"
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
        plt.show()
        startDate=startDate+day
        endDate=endDate+day




#plotEachDay()
calcCorrelation()
#plot24Hour()



