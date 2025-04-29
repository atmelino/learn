# Using stylegan3 for this module because stylegan2 did not work on my systems
echo conda environment for this program:
echo conda activate stylegan3


mkdir ../../../../../local_data/practice/stylegan3_dogs_small_small
mkdir ../../../../../local_data/practice/stylegan3_dogs_small/images
mkdir ../../../../../local_data/practice/stylegan3_dogs_small/datasets
mkdir ../../../../../local_data/practice/stylegan3_dogs_small/output


code_path="../../../../../local_data/stylegan3/dataset_tool.py"
source_path="../../../../../local_data/practice/stylegan3_dogs_small/images"
destination_path="../../../../../local_data/practice/stylegan3_dogs_small/datasets/dogs-32x32.zip"

python $code_path --source=$source_path --dest=$destination_path  --resolution=32x32
