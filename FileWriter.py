import definitions
import pandas as pd


def writeToFile(input, filename):
    ROOT_DIR = definitions.ROOT_DIR
    file = "%s/Output/%s.csv" % (ROOT_DIR, filename)
    #prediction = pd.DataFrame(index=X_test.index)
    #prediction["is_fake"] = y_test
    input.to_csv(file, header='timestamp \t power', sep=',')


def writePreparedInput(train, filename):
    ROOT_DIR = definitions.ROOT_DIR
    file = "%s/Input/%s.csv" % (ROOT_DIR, filename)

    train.to_csv(file, sep=',')