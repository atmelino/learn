
snowy_path="../../../../../local_data/practice/stylegan3_02"
code_path="../../../../../local_data/stylegan3/dataset_tool.py"
source_path="../../../../../local_data/practice/stylegan3_02/images1024x1024"
destination_path="../../../../../local_data/practice/stylegan3_02/datasets/snowy-256x256.zip"

python $code_path --source=$source_path --dest=$destination_path  --resolution=256x256




python dataset_tool.py --source=path/to/source  --dest=path/to/destination.zip --resolution=256x256
