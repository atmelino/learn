



print("class_06_3_resnet")
# this program requires the file structure to exist, that is created by running class_06_2_cnn_A_prepare.py

PATH = "./not_on_github"
EXTRACT_TARGET = os.path.join(PATH, "clips")
SOURCE = os.path.join(PATH, "clips/paperclips")
TARGET = os.path.join(PATH, "clips-processed")

df_train = pd.read_csv(os.path.join(SOURCE, "train.csv"))
df_train['filename'] = "clips-" + df_train.id.astype(str) + ".jpg"
print(df_train)

