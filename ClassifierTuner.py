from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
import TunedClassifier


def tuneClassifier(X_train, classifier, grid, features, y_train):
    gridSearch = GridSearchCV(classifier, param_grid=grid, scoring="r2", n_jobs=4, verbose=1)
    gridSearch.fit(X_train[features], y_train)
    return TunedClassifier.TunedClassifier(gridSearch.best_estimator_, gridSearch.best_score_)


def getLinearRegressionGrid():
    return {
        "fit_intercept" : [True,False],
        "normalize": [True,False]
    }

def getSVCGrid():
    return {
        "kernel": ["rbf"],
        "gamma": [0.003, 0.004],
        "C": [2, 3],
        "degree": [1, 2],
        "random_state": [2, 3],
        "coef0": [0.0],
        "cache_size": [35, 45],
        "class_weight": ["balanced", None]
    }


def getExtraTreeGrid():
    return {
        "max_depth": [8, 12],
        "max_features": [6, 10],
        "min_samples_split": [6, 7],
        "min_samples_leaf": [6, 7],
        "bootstrap": [False],
        "n_estimators": [90, 100],
        "random_state": [1, 2, 3],
        "criterion": ["gini"]}


def getGradientBoostingGrid():
    return {
        "loss": ["deviance"],
        "n_estimators": [250, 300],
        "learning_rate": [0.10, 0.15],
        "max_depth": [5, 6, 7],
        "min_samples_leaf": [80],
        "max_features": [0.30],
        "random_state": [4, 5]
    }


def getRandomForestGrid():
    return {
        "random_state": [9],
        "max_depth": [14],
        "max_features": [2, 3, 4],
        "min_samples_split": [2, ],
        "min_samples_leaf": [2],
        "bootstrap": [False],
        "n_estimators": [66],
        "criterion": ["entropy"]}


def getDecisionTreeGrid():
    return {
        "max_depth": [5, 10, 15],
        "max_features": [8, 10, 12],
        "min_samples_split": [2, 3],
        "min_samples_leaf": [1, 2],
        "min_weight_fraction_leaf": [0.05, 0.01, 0.015],
        "min_impurity_decrease": [0.0],
        "random_state": [2, 3],
        "presort": [False, True],
        "criterion": ["entropy"]
    }


def getMLPGrid():
    return {
        "activation": ["tanh"],
        "hidden_layer_sizes": [(100,), (80,), (120,)],
        "alpha": [0.0001],
        "solver": ["lbfgs"],
        "max_iter": [400],
        "random_state": [4],
        "momentum": [0.5, 0.6, 0.7]
    }


def getLinearDiscriminantAnalysisTuner():
    return {
        "solver": ["eigen"],
        "n_components": [1, 2, 3],
        "shrinkage": ["auto", 0.5, 0.55, 0.6, 0.65],
        "tol": [0.0001]
    }


def getLogisticRegressionGrid():
    return {
        "solver": ["lbfgs"],
        "penalty": ["l2"],
        "verbose": [0.3, 0.4, 0.5],
        "tol": [0.0001],
        "C": [0.5, 0.63],
        "class_weight": ["balanced", None],
        "max_iter": [500, 1000],
        "multi_class": ["ovr", "multinomial"]
    }


def getKNeighborsClassifierGrid():
    return {
        "algorithm": ["ball_tree"],
        "n_neighbors": [6, 7, 8],
        "weights": ["distance"],
        "leaf_size": [15, 20, 25],
        "p": [1]
    }


def getAdaBoostGrid():
    return {
        "base_estimator__criterion": ["gini", "entropy"],
        "n_estimators": [9, 10, 11],
        "learning_rate": [1.4, 1.5, 1.6],
        "algorithm": ["SAMME", "SAMME.R"],
        "base_estimator__splitter": ["best", "random"],
        "random_state": [9, 10, 11]
    }


def getGaussianNBGrid():
    return {}


def getMultinomialNBGrid():
    return {
        "alpha": [0.0, 0.2, 0.5, 0.75, 1.0],
        "fit_prior": [True, False]
    }


def getBernoulliNBGrid():
    return {
        "alpha": [0.2, 0.5, 0.75, 1.0],
        "fit_prior": [True, False]
    }
