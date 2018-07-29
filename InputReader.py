import pandas as pd
import definitions


def read(filename, index_col):
    ROOT_DIR = definitions.ROOT_DIR
    file = "%s/Input/%s.csv" % (ROOT_DIR, filename)
    train = pd.read_csv(file, index_col=index_col)
    return train