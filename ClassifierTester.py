# this script is for testing different tuned classifiers. Score is calculated on a test  dataset,
# that is splitted from the train dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import TunedClassifiers
import InputReader


train=InputReader.read("fridgeEnergyTrain24H","timestamp")
train=train.dropna(axis=0)

features = ["humidity"]

y_train = train['energy']
X_train = train[features]
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, random_state=0)

#classifier = TunedClassifiers.getTunedDecisionTree()

classifier=LinearRegression()

classifier.fit(X_train, y_train)

print('Accuracy of classifier on training set: {:.2f}'
      .format(classifier.score(X_train, y_train)))
