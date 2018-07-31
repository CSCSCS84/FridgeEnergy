# Runs a prediction for the energy that the fridge is consuming. A LinearRegression model is taken because this model had
# the best R2 score on the train data set. Period length in the dataset is 14400 seconds = 4 Hours, the values are summed up.
# The Result is written to file Output/prediction_%s with s=frequence .
import InputReader
import PrepareInput
from sklearn.linear_model import LinearRegression
import pandas as pd
import FileWriter
from pandas import Grouper
import Constants


def run():
    freq = "14400s"
    print("Prepare Input")
    trainGrouped = prepareTrain(freq)
    testGrouped = prepareTest(freq)
    print("Run regression algorithm \n")
    yPrediction = runRegression(trainGrouped, testGrouped)
    predictionGrouped = groupPrediction(testGrouped, yPrediction)
    writeToFile(predictionGrouped, freq)
    return predictionGrouped


def runRegression(trainGrouped, testGrouped):
    features = ["humidity", "temperature"]
    regression = LinearRegression()
    regression.fit(trainGrouped[features], trainGrouped["energy"])
    yPrediction = regression.predict(testGrouped)
    return yPrediction


def groupPrediction(testGrouped, yPrediction):
    result = toDataFrame(testGrouped, yPrediction)
    result.index = pd.to_datetime(testGrouped.index)
    predictionGrouped = result.groupby(Grouper(freq="1D", axis=0))
    predictionGrouped = predictionGrouped.agg(lambda x: x.sum()).round(2)
    return predictionGrouped


def toDataFrame(test, yPrediction):
    result = pd.DataFrame(test.index)
    result['energy'] = yPrediction.round(2)
    return result


def writeToFile(result, freq):
    FileWriter.writeToFile(result, "prediction_%s" % (freq))


def prepareTrain(freq):
    PrepareInput.prepareData(freq)
    train = InputReader.read("%s_%s" % (Constants.fileNameTrain, freq), "timestamp")
    train = train.dropna(axis=0)
    return train


def prepareTest(freq):
    test = InputReader.read("weather_forecasts_Berlin_Tegel_per_hour", "timestamp")
    test.index = pd.to_datetime(test.index)
    testGrouped = PrepareInput.groupWeatherData(test, freq)
    return testGrouped


prediction = run()
print("Energy (in Joule) Prediction for 2017-08-02 to 2017-08-11:")
print(prediction)
