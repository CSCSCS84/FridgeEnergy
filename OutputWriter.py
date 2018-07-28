import definitions
import pandas as pd


def writeToFile(input, filename):
    ROOT_DIR = definitions.ROOT_DIR
    file = "%s/Output/%s.csv" % (ROOT_DIR, filename)
    #prediction = pd.DataFrame(index=X_test.index)
    #prediction["is_fake"] = y_test
    input.to_csv(file, header='timestamp \t power', sep=',')
