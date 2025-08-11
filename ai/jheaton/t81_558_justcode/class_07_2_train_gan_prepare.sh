# Original 1024x1024 resolution.

# Scaled down 256x256 resolution.

code_path="../../../../local_data/packages/stylegan3/dataset_tool.py"
source_path="../../../../local_data/jheaton/class_07_2_train_gan/images/dogs"
destination_path="../../../../local_data/jheaton/class_07_2_train_gan/datasets/dogs-256x256.zip"

python $code_path --source=$source_path --dest=$destination_path  --resolution=256x256




