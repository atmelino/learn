# Using stylegan3 for this module because stylegan2 did not work on my systems
echo conda environment for this program:
echo conda activate stylegan3


mkdir ../../../../local_data/jheaton/class_07_2_train_gan/images/dogs
mkdir ../../../../local_data/jheaton/class_07_2_train_gan/datasets
mkdir ../../../../local_data/jheaton/class_07_2_train_gan/output


code_path="../../../../local_data/stylegan3/dataset_tool.py"
source_path="../../../../local_data/jheaton/class_07_2_train_gan/images/dogs"
destination_path="../../../../local_data/jheaton/class_07_2_train_gan/datasets/dogs-256x256.zip"

python $code_path --source=$source_path --dest=$destination_path  --resolution=256x256
