echo conda activate stylegan3

# Original 1024x1024 resolution.
# python3  dataset_tool.py --source=/tmp/images1024x1024 --dest=~/datasets/ffhq-1024x1024.zip

# Scaled down 256x256 resolution.

# flickrfaces_path="../../../../../local_data/practice/stylegan3_ffhq_small" 
# code_path="../../../../../local_data/stylegan3/dataset_tool.py"  
# source_path="../../../../../local_data/practice/stylegan3_ffhq_small/images1024x1024" 
# destination_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-256x256_small.zip"

# python $code_path --source=$source_path --dest=$destination_path  --resolution=256x256


# Scaled down 128x128 resolution.

# flickrfaces_path="../../../../../local_data/practice/stylegan3_ffhq_small" 
# code_path="../../../../../local_data/stylegan3/dataset_tool.py"  
# source_path="../../../../../local_data/practice/stylegan3_ffhq_small/images1024x1024" 
# destination_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-128x128_small.zip"

# python $code_path --source=$source_path --dest=$destination_path  --resolution=128x128

# Scaled down 32x32 resolution. 

flickrfaces_path="../../../../../local_data/practice/stylegan3_ffhq_small"
code_path="../../../../../local_data/stylegan3/dataset_tool.py" 
source_path="../../../../../local_data/practice/stylegan3_ffhq_small/images1024x1024"
destination_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-32x32_small.zip" 

python $code_path --source=$source_path --dest=$destination_path  --resolution=32x32
