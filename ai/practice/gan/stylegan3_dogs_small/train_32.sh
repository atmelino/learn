# Use stylegan3 conda environment
echo conda environment for this program:
echo conda activate stylegan3


# Modify these to suit your needs
code_path="../../../../../local_data/stylegan3/train.py"
data_path="../../../../../local_data/practice/stylegan3_dogs_small/datasets/dogs-32x32.zip"
outdir_path="../../../../../local_data/practice/stylegan3_dogs_small/output"
options="--cfg=stylegan2 --gpus=2 --batch=8 --gamma=10 --mirror=1 --aug=noaug --kimg=200 --snap=1"

python3 $code_path --outdir=$outdir_path --data=$data_path $options

