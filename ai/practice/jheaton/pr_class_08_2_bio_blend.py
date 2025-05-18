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

SHUFFLE = False
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


def stretch(y):
    print("stretch() y parameter\n",y)
    print("y.min ",y.min())    
    print("y.max ",y.max())    
    return (y - y.min()) / (y.max() - y.min())


def blend_ensemble(x, y, x_submit):
    kf = StratifiedKFold(FOLDS)
    kf.get_n_splits(x)
    print(kf)
    for i, (train_index, test_index) in enumerate(kf.split(x)):
        print(f"Fold {i}:")
        print(f"  Train: index={train_index}")
        print(f"  Test:  index={test_index}")

    exit()



    folds = list(kf.split(x, y))

    print("kf.split(x, y)",kf.split(x, y))
    print("folds.shape ",np.array(folds).shape)
    print("folds",folds)
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

    dataset_blend_train = np.zeros((x.shape[0], len(models)))
    dataset_blend_test = np.zeros((x_submit.shape[0], len(models)))

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

    print()
    print("Blending models.")
    blend = LogisticRegression(solver="lbfgs")
    blend.fit(dataset_blend_train, y)
    return blend.predict_proba(dataset_blend_test)


if __name__ == "__main__":

    BASE_PATH = "../../../../local_data/jheaton"
    OUTPUT_PATH = os.path.join(BASE_PATH, "class_08_2_keras_ensembles_bio_blend/")
    os.system("mkdir -p " + OUTPUT_PATH)

    np.random.seed(42)

    # seed to shuffle the train set
    print("Loading data...")
    # URL = "https://data.heatonresearch.com/data/t81-558/kaggle/"
    URL = "../../../../local_data/jheaton/input/"
    df_train = pd.read_csv(URL + "bio_train.csv", na_values=["NA", "?"])
    df_submit = pd.read_csv(URL + "bio_test.csv", na_values=["NA", "?"])

    predictors = list(df_train.columns.values)
    predictors.remove("Activity")
    x = df_train[predictors].values
    y = df_train["Activity"]
    x_submit = df_submit.values

    if SHUFFLE:
        idx = np.random.permutation(y.size)
        x = x[idx]
        y = y[idx]

    submit_data_original = blend_ensemble(x, y, x_submit)
    submit_data = stretch(submit_data_original)

    ####################
    # Build submit file
    ####################
    ids = [id + 1 for id in range(submit_data.shape[0])]
    submit_df = pd.DataFrame(
        {"MoleculeId": ids, "PredictedProbability": submit_data[:, 1]},
        columns=["MoleculeId", "PredictedProbability"],
    )

    submit_df.to_csv(OUTPUT_PATH + "submit.csv", index=False)

    # Debug section
    # print("x", x.shape)
    # print("y", y.shape)
    # print("x_submit", x_submit.shape)
    # print("submit_data shape\n",submit_data_original.shape)    
    # print("submit_data\n",submit_data_original)    
    # submit_data_original_df = pd.DataFrame(submit_data_original)
    # submit_data_original_df.to_csv(OUTPUT_PATH + "blend_ensemble_original.csv", index=False)
    # print("submit_data stretched shape\n",submit_data.shape)    
    # print("submit_data\n",submit_data)    
    # submit_data_df = pd.DataFrame(submit_data)
    # submit_data_df.to_csv(OUTPUT_PATH + "blend_ensemble_stretched.csv", index=False)

    # print("submit_data[:, 1]", submit_data[:, 1])




