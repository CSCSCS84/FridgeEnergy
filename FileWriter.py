import definitions


def writeToFile(input, filename):
    ROOT_DIR = definitions.ROOT_DIR
    file = "%s/Output/%s.csv" % (ROOT_DIR, filename)
    input.to_csv(file, header='timestamp \t energy', sep=',')


def writePreparedInput(train, filename):
    ROOT_DIR = definitions.ROOT_DIR
    file = "%s/Input/%s.csv" % (ROOT_DIR, filename)
    train.to_csv(file, sep=',')


def writeToFileForClassifierTester(input, filename):
    ROOT_DIR = definitions.ROOT_DIR
    file = "%s/Output/%s.csv" % (ROOT_DIR, filename)
    input.to_csv(file, sep=',')