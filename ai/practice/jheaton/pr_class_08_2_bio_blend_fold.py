print("conda environment for this program:")
print("conda activate ensemble")

import numpy as np
import os
import pandas as pd
import math
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
# from scikeras.wrappers import KerasClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping

print("pr_class_08_2_bio_blend_fold")

# Options for this run
length = 100
FOLDS = 10
SHORT= True

def build_ann(input_size, classes, neurons):
    model = Sequential()
    model.add(Dense(neurons, input_dim=input_size, activation="relu"))
    model.add(Dense(1))
    model.add(Dense(classes, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    return model


def mlogloss(y_test, preds):
    epsilon = 1e-15
    sum = 0
    for row in zip(preds, y_test):
        x = row[0][row[1]]
        x = max(epsilon, x)
        x = min(1 - epsilon, x)
        sum += math.log(x)
    return (-1 / len(preds)) * sum


def blend_ensemble(x, y, x_submit):
    kf = StratifiedKFold(FOLDS)
    folds = list(kf.split(x, y))

    if(SHORT==True):
        models = [
            KerasClassifier(
                build_fn=build_ann, neurons=20, input_size=x.shape[1], classes=2
            ),
            KNeighborsClassifier(n_neighbors=3),
            RandomForestClassifier(n_estimators=100, n_jobs=-1, criterion="gini"),
            RandomForestClassifier(n_estimators=100, n_jobs=-1, criterion="entropy"),
            ExtraTreesClassifier(n_estimators=100, n_jobs=-1, criterion="gini"),
            ExtraTreesClassifier(n_estimators=100, n_jobs=-1, criterion="entropy"),
        ]
    else:
        models = [
            KerasClassifier(
                build_fn=build_ann, neurons=20, input_size=x.shape[1], classes=2
            ),
            KNeighborsClassifier(n_neighbors=3),
            RandomForestClassifier(n_estimators=100, n_jobs=-1, criterion="gini"),
            RandomForestClassifier(n_estimators=100, n_jobs=-1, criterion="entropy"),
            ExtraTreesClassifier(n_estimators=100, n_jobs=-1, criterion="gini"),
            ExtraTreesClassifier(n_estimators=100, n_jobs=-1, criterion="entropy"),
            GradientBoostingClassifier(
                learning_rate=0.05, subsample=0.5, max_depth=6, n_estimators=50
            ),
        ]

    print("x.shape[0]",x.shape[0])
    print("x.shape[1]",x.shape[1])
    print("x_submit.shape[0]",x_submit.shape[0])
    print("x_submit.shape[1]",x_submit.shape[1])
    print("len(models)",len(models))
    dataset_blend_train = np.zeros((x.shape[0], len(models)))
    dataset_blend_test = np.zeros((x_submit.shape[0], len(models)))
    # print("dataset_blend_train",dataset_blend_train)

    for j, model in enumerate(models):
        print("Model: {} : {}".format(j, model))
        fold_sums = np.zeros((x_submit.shape[0], len(folds)))

        total_loss = 0
        for i, (train, test) in enumerate(folds):
            x_train = x[train]
            y_train = y[train]
            x_test = x[test]
            y_test = y[test]
            # print("x_train.shape", x_train.shape)
            # print("y_train.shape", y_train.shape)
            # print("x_test.shape", x_test.shape)
            # print("y_test.shape", y_test.shape)
            model.fit(x_train, y_train)
            
            pred = np.array(model.predict_proba(x_test))
            # print("pred",pred)
            dataset_blend_train[test, j] = pred[:, 1]

            pred2 = np.array(model.predict_proba(x_submit))
            fold_sums[:, i] = pred2[:, 1]

            loss = mlogloss(y_test, pred)
            total_loss += loss
            print("Fold #{}: loss={}".format(i, loss))
        print(
            "{}: Mean loss={}".format(model.__class__.__name__, total_loss / len(folds))
        )
        dataset_blend_test[:, j] = fold_sums.mean(1)

    exit()

    print()
    print("Blending models.")
    blend = LogisticRegression(solver="lbfgs")
    blend.fit(dataset_blend_train, y)
    return blend.predict_proba(dataset_blend_test)


def show_folds(x, y, x_submit):
    kf = StratifiedKFold(FOLDS)
    kf.get_n_splits(x)
    print(kf)
    for i, (train_index, test_index) in enumerate(kf.split(x,y)):
        print(f"Fold {i}:")
        print(f"  Train: index={train_index}")
        print(f"  Test:  index={test_index}")

    folds = list(kf.split(x, y))
    print("folds",folds)




if __name__ == "__main__":

    BASE_PATH = "../../../../local_data/practice/jheaton"
    OUTPUT_PATH = os.path.join(BASE_PATH, "pr_class_08_2_bio_blend_fold/")
    os.system("mkdir -p " + OUTPUT_PATH)

    print("Loading data...")
    URL = "../../../../local_data/jheaton/input/"
    df_train = pd.read_csv(URL + "bio_train.csv", na_values=["NA", "?"])
    df_submit = pd.read_csv(URL + "bio_test.csv", na_values=["NA", "?"])

    # df_train = df_train.iloc[0:length]
    # df_submit = df_submit.iloc[0:length]

    predictors = list(df_train.columns.values)
    predictors.remove("Activity")
    x = df_train[predictors].values
    y = df_train["Activity"]
    x_submit = df_submit.values

    # submit_data = show_folds(x, y, x_submit)
    submit_data = blend_ensemble(x, y, x_submit)






