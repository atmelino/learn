# conda activate stylegan3

# Train StyleGAN2 for dogs at 256x256 resolution using 1 GPU.

code_path="../../../../local_data/packages/stylegan3/train.py"
outdir_path="../../../../local_data/jheaton/class_07_2_train_gan/training-runs"
data_path="../../../../local_data/jheaton/class_07_2_train_gan/datasets/dogs-256x256.zip"

options="--cfg=stylegan2 --gpus=1 --batch=32 --gamma=10 --mirror=1 --aug=noaug"

python3 $code_path --outdir=$outdir_path --data=$data_path $options


