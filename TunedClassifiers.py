#Functions returning the tuned classifiers
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def getTunedSVC():
    return SVC(C=3, cache_size=35, class_weight='balanced', coef0=0.0,
               decision_function_shape='ovr', degree=1, gamma=0.003, kernel='rbf',
               max_iter=-1, probability=False, random_state=2, shrinking=True,
               tol=0.001, verbose=False)


def getTunedDecisionTree():
    return DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=5,
            max_features=10, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.01, presort=False, random_state=2,
            splitter='best')


def getTunedKNeighbors():
    return KNeighborsClassifier(algorithm='ball_tree', leaf_size=15, metric='minkowski',
                         metric_params=None, n_jobs=1, n_neighbors=7, p=1,
                         weights='distance')


def getTunedLogisticRegression():
    return LogisticRegression(C=0.63, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=500, multi_class='ovr', n_jobs=1,
          penalty='l2', random_state=None, solver='lbfgs', tol=0.0001,
          verbose=0.3, warm_start=False)
