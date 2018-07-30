# this script is for testing different classifiers. Score is calculated on a test  dataset,
# that is splitted from the train dataset. R2 score is taken.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import  BayesianRidge
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
import InputReader
import pandas as pd
import FileWriter

train = InputReader.read("fridgeEnergyTrain14400s", "timestamp")
train = train.dropna(axis=0)

features = ["humidity", "temperature"]

y_train = train['energy']
X_train = train[features]
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, random_state=0)
classifiers = [LinearRegression(), Lasso(), RandomForestRegressor(), KNeighborsRegressor(),
               DecisionTreeRegressor(),BayesianRidge(),SVR(),MLPRegressor()]

yPred = pd.DataFrame(index=X_test.index)
i = 1
for classifier in classifiers:
    classifier.fit(X_train, y_train)
    y = classifier.predict(X_test)
    yPred["prediction%s" % (i)] = y.round(2)
    i = i + 1
result = pd.concat([X_test, yPred], axis=1)
print(result)
FileWriter.writeToFileForClassifierTester(result,"result14400s")

# random forest dont need scaling!
for classifier in classifiers:
    classifier.fit(X_train, y_train)
    print('Accuracy of classifier on training set: {:.2f}'
          .format(classifier.score(X_test, y_test)))
