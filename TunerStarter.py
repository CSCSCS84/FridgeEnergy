#Tunes the classifiers.
# The training set has to be prepared and is not the original dataset.
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import Constants
import InputReader
import ClassifierTuner
from sklearn.linear_model import LinearRegression

freq="14400s"
filename = Constants.fileNameTrain+"%s" % (freq)
train = InputReader.read(filename,Constants.indexName)
train=train.dropna(axis=0)

features = ["temperature","humidity"]

y_train = train["energy"]
searchGrid = ClassifierTuner.getLinearRegressionGrid()
classifier = LinearRegression()

tunedClassifier = ClassifierTuner.tuneClassifier(train, classifier, searchGrid, features, y_train)
print(tunedClassifier)
