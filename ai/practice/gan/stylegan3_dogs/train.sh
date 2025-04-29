# Using stylegan3 for this module because stylegan2 did not work on my systems
echo conda environment for this program:
echo conda activate stylegan3


# Modify these to suit your needs
code_path="../../../../../local_data/stylegan3/train.py"
data_path="../../../../../local_data/practice/stylegan3_dogs/datasets/dogs-256x256.zip"
outdir_path="../../../../../local_data/practice/stylegan3_dogs/output"
options="--cfg=stylegan2 --gpus=2 --batch=8 --gamma=10 --mirror=1 --aug=noaug --kimg=200 --snap=1"

python3 $code_path --outdir=$outdir_path --data=$data_path $options

