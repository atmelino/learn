# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from scipy.stats import zscore
import numpy as np
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

pd.set_option('display.expand_frame_repr', False)
np.set_printoptions(linewidth=np.inf)
np.set_printoptions(threshold=np.inf)

print_number=0
plot_number=0
# Plot a confusion matrix.
# cm is the confusion matrix, names are the names of the classes.
def plot_confusion_matrix(cm, names, title='Confusion matrix', 
                            cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(names))
    plt.xticks(tick_marks, names, rotation=45)
    plt.yticks(tick_marks, names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    

# Plot an ROC. pred - the predictions, y - the expected output.
def plot_roc(pred,y):
    fpr, tpr, _ = roc_curve(y, pred)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc="lower right")
    plt.show()


plot1=False
if plot1:
    mu1 = -2
    mu2 = 2
    variance = 1
    sigma = math.sqrt(variance)
    x1 = np.linspace(mu1 - 5*sigma, mu1 + 4*sigma, 100)
    x2 = np.linspace(mu2 - 5*sigma, mu2 + 4*sigma, 100)
    plt.plot(x1, stats.norm.pdf(x1, mu1, sigma)/1,color="green", 
            linestyle='dashed')
    plt.plot(x2, stats.norm.pdf(x2, mu2, sigma)/1,color="red")
    plt.axvline(x=-2,color="black")
    plt.axvline(x=0,color="black")
    plt.axvline(x=+2,color="black")
    plt.text(-2.7,0.55,"Sensitive")
    plt.text(-0.7,0.55,"Balanced")
    plt.text(1.7,0.55,"Specific")
    plt.ylim([0,0.53])
    plt.xlim([-5,5])
    plt.legend(['Negative','Positive'])
    plt.yticks([])
    if print_number==1:
        plt.show()


roc_example=False
if roc_example==True:
    df = pd.read_csv(
        "https://data.heatonresearch.com/data/t81-558/wcbreast_wdbc.csv",
        na_values=['NA','?'])

    # pd.set_option('display.max_columns', 5)
    # pd.set_option('display.max_rows', 5)
    if print_number==2:
        print(df)

    x_columns = df.columns.drop('diagnosis').drop('id')
    for col in x_columns:
        df[col] = zscore(df[col])
    if print_number==3:
        print(df)

    # Convert to numpy - Regression
    x = df[x_columns].values
    y = df['diagnosis'].map({'M':1,"B":0}).values # Binary classification, M is 1 and B is 0
    # print(x)

    # Classification neural network

    # Split into train/test
    x_train, x_test, y_train, y_test = train_test_split(    
        x, y, test_size=0.25, random_state=42)

    model = Sequential()
    model.add(Dense(100, input_dim=x.shape[1], activation='relu',
                    kernel_initializer='random_normal'))
    model.add(Dense(50,activation='relu',kernel_initializer='random_normal'))
    model.add(Dense(25,activation='relu',kernel_initializer='random_normal'))
    model.add(Dense(1,activation='sigmoid',kernel_initializer='random_normal'))
    model.compile(loss='binary_crossentropy', 
                optimizer=tensorflow.keras.optimizers.Adam(),
                metrics =['accuracy'])
    monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, 
        patience=5, verbose=1, mode='auto', restore_best_weights=True)

    model.fit(x_train,y_train,validation_data=(x_test,y_test),
            callbacks=[monitor],verbose=0,epochs=1000)


    pred = model.predict(x_test)
    # print(pred)

    df2 = pd.DataFrame(pred)
    # print(df2)
    df2['pred']=pred
    df2['y_test']= y_test
    # pd.set_option('display.max_rows', 100)
    print(df2)

    if plot_number==1:
        plot_roc(pred,y_test)




multiclass=True
# if multiclass:


# Read the data set
df = pd.read_csv(
    "https://data.heatonresearch.com/data/t81-558/jh-simple-dataset.csv",
    na_values=['NA','?'])

# Generate dummies for job
df = pd.concat([df,pd.get_dummies(df['job'],prefix="job")],axis=1)
df.drop('job', axis=1, inplace=True)

# Generate dummies for area
df = pd.concat([df,pd.get_dummies(df['area'],prefix="area")],axis=1)
df.drop('area', axis=1, inplace=True)

# Missing values for income
med = df['income'].median()
df['income'] = df['income'].fillna(med)

# Standardize ranges
df['income'] = zscore(df['income'])
df['aspect'] = zscore(df['aspect'])
df['save_rate'] = zscore(df['save_rate'])
df['age'] = zscore(df['age'])
df['subscriptions'] = zscore(df['subscriptions'])
# print(df)

# Convert to numpy - Classification
x_columns = df.columns.drop('product').drop('id')
x = df[x_columns].values
dummies = pd.get_dummies(df['product']) # Classification
print(dummies)
products = dummies.columns
y = dummies.values
# print(y.shape)

# Classification neural network
import numpy as np
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(    
    x, y, test_size=0.25, random_state=42)

x_train = np.asarray(x_train).astype(np.float32)
y_train = np.asarray(y_train).astype(np.float32)
x_test = np.asarray(x_test).astype(np.float32)
y_test = np.asarray(y_test).astype(np.float32)

model = Sequential()
model.add(Dense(100, input_dim=x.shape[1], activation='relu',
                kernel_initializer='random_normal'))
model.add(Dense(50,activation='relu',kernel_initializer='random_normal'))
model.add(Dense(25,activation='relu',kernel_initializer='random_normal'))
print("NN will have %d outputs" % y.shape[1])
model.add(Dense(y.shape[1],activation='softmax',
                kernel_initializer='random_normal'))
model.compile(loss='categorical_crossentropy', 
            optimizer=tensorflow.keras.optimizers.Adam(),
            metrics =['accuracy'])
monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, patience=5, 
                        verbose=1, mode='auto', restore_best_weights=True)
model.fit(x_train,y_train,validation_data=(x_test,y_test),
        callbacks=[monitor],verbose=2,epochs=1000)

pred = model.predict(x_test)
np.set_printoptions(suppress=True)
np.set_printoptions(precision=3)
print(pred)
pred = np.argmax(pred,axis=1) 
# raw probabilities to chosen class (highest probability)









