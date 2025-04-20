# Original 1024x1024 resolution.
# python3  not_on_github/stylegan3/dataset_tool.py --source=/tmp/images1024x1024 --dest=~/datasets/ffhq-1024x1024.zip

# Scaled down 256x256 resolution.

flickrfaces_path="../../../../../local_data/practice/stylegan3_ffhq"
code_path="../../../../../local_data/stylegan3/dataset_tool.py"
source_path="../../../../../local_data/practice/stylegan3_ffhq/images1024x1024"
destination_path="../../../../../local_data/practice/stylegan3_ffhq/datasets/ffhq-256x256.zip"

python $code_path --source=$source_path --dest=$destination_path  --resolution=256x256




