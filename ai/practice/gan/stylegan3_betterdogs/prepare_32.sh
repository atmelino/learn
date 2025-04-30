# Using stylegan3 for this module because stylegan2 did not work on my systems
echo conda environment for this program:
echo conda activate stylegan3


mkdir ../../../../../local_data/practice/stylegan3_betterdogs
mkdir ../../../../../local_data/practice/stylegan3_betterdogs/images
mkdir ../../../../../local_data/practice/stylegan3_betterdogs/datasets
mkdir ../../../../../local_data/practice/stylegan3_betterdogs/output


code_path="../../../../../local_data/stylegan3/dataset_tool.py"
source_path="../../../../../local_data/practice/stylegan3_betterdogs/images"
destination_path="../../../../../local_data/practice/stylegan3_betterdogs/datasets/dogs-32x32.zip"

python $code_path --source=$source_path --dest=$destination_path  --resolution=32x32
