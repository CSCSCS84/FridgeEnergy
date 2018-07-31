# this script is for testing different regression algorithm. Score is calculated on a test dataset,
# that is splitted from the train dataset. R2 score is taken.
# Note: Some of the files might not be created. Use PrepareInput to create a file with a given frequence
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import BayesianRidge
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
import InputReader
import Scaler

train = InputReader.read("fridgeEnergyTrain_14400s", "timestamp")
train = train.dropna(axis=0)
features = ["humidity", "temperature"]

y_train = train['energy']
X_train = train[features]
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, random_state=0)
regressions = [LinearRegression(), Lasso(), RandomForestRegressor(), KNeighborsRegressor(),
               DecisionTreeRegressor(), BayesianRidge(), SVR(), MLPRegressor()]

for reg in regressions:
    reg.fit(X_train, y_train)
    print('Accuracy of classifier on training set: {:.2f}'
          .format(reg.score(X_test, y_test)))
