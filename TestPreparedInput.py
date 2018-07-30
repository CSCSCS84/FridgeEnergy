# short script for testing the prepared input
import Constants
import InputReader
import numpy as np


def test60sData():
    filename = "fridgeEnergyTrain60s"
    data = InputReader.read(filename, Constants.indexName)

    if data.loc["2017-07-01 00:00:00"]['temperature'] != 14.5:
        print("Error in %s" % (filename))

    if ~(np.isnan(data.loc["2017-07-01 00:01:00"]['temperature'])):
        print("Error in %s" % (filename))

    if data.loc["2017-07-06 18:00:00"]['humidity'] != 40.0:
        print("Error in %s" % (filename))

    if data.loc["2017-07-01 00:00:00"]['energy'] != 3837.18:
        print("Error in %s" % (filename))

    if data.loc["2017-07-06 00:09:00"]['energy'] != 71.64:
        print("Error in %s" % (filename))

def test3600sData():
    filename = "fridgeEnergyTrain3600s"
    data = InputReader.read(filename, Constants.indexName)

    if data.loc["2017-07-01 00:00:00"]['energy'] != 10146.35:
        print("Error in %s" % (filename))
    if data.loc["2017-07-28 20:00:00"]['energy'] != 117893.96:
        print("Error in %s" % (filename))

    if data.loc["2017-07-01 00:00:00"]['temperature'] != 14.3:
        print("Error in %s" % (filename))
    if data.loc["2017-07-01 00:00:00"]['humidity'] != 95.0:
        print("Error in %s" % (filename))

    if data.loc["2017-07-28 20:00:00"]['temperature'] != 16.3:
        print("Error in %s" % (filename))
    if data.loc["2017-07-28 20:00:00"]['humidity'] != 82.0:
        print("Error in %s" % (filename))

def test14400sData():
    filename = "fridgeEnergyTrain14400s"
    data = InputReader.read(filename, Constants.indexName)
    if data.loc["2017-07-01 00:00:00"]['energy'] != 282273.06:
        print("Error in %s" % (filename))

    if data.loc["2017-07-01 00:00:00"]['temperature'] != 14.26:
        print("Error in %s" % (filename))
    if data.loc["2017-07-01 00:00:00"]['humidity'] != 94.5:
        print("Error in %s" % (filename))

    if data.loc["2017-07-06 12:00:00"]['temperature'] != 24.64:
        print("Error in %s" % (filename))
    if data.loc["2017-07-06 12:00:00"]['humidity'] != 38.88:
        print("Error in %s" % (filename))


test60sData()
test3600sData()
test14400sData()

