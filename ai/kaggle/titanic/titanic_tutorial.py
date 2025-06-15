# conda environment for this program:
# conda activate jh_class

import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

BASE_PATH = "../../../../local_data/kaggle/titanic/"
DATA_PATH = os.path.join(BASE_PATH, "input/")
OUTPUT_PATH = os.path.join(BASE_PATH, "titanic_tutorial/")
os.system("mkdir -p " + OUTPUT_PATH)


# train_data = pd.read_csv("/kaggle/input/titanic/train.csv")
train_data = pd.read_csv(DATA_PATH + "train.csv", na_values=["NA", "?"])
train_data.head()

# test_data = pd.read_csv("/kaggle/input/titanic/test.csv")
test_data = pd.read_csv(DATA_PATH + "test.csv", na_values=["NA", "?"])
test_data.head()

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)

from sklearn.ensemble import RandomForestClassifier

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
# output.to_csv('submission.csv', index=False)
output.to_csv(OUTPUT_PATH + "submission.csv", index=False)
print("Your submission was successfully saved!")

