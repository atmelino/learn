import os

print("class_06_2_cnn_animals")

BASE_PATH = "../../../../local_data/jheaton"
DATA_PATH = os.path.join(BASE_PATH, "animals")
OUTPUT_PATH=os.path.join(BASE_PATH, "class_06_2_cnn_animals")

# Create the directories
cmd1="mkdir -p "+ DATA_PATH
cmd2="mkdir -p "+ OUTPUT_PATH

print(cmd1)
print(cmd2)

os.system(cmd1)
os.system(cmd2)

# Copy the cats and dogs images into the animals folder before running the training
