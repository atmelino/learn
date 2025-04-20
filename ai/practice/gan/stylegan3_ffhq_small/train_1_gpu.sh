# conda activate stylegan3

# Train StyleGAN2 for FFHQ at 256x256 resolution using 1 GPU.
# outdir_path="../../../../../local_data/practice/test_stylegan3_ffhq/training-runs"
# data_path="../../../../../local_data/practice/test_stylegan3_ffhq/datasets/ffhq-256x256.zip"

code_path="../../../../../local_data/stylegan3/train.py"
outdir_path="../../../../../local_data/practice/stylegan3_ffhq_small/training-runs"
data_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-256x256_small.zip"
options="--cfg=stylegan2 --gpus=1 --batch=32 --gamma=10 --mirror=1 --aug=noaug"

python3 $code_path --outdir=$outdir_path --data=$data_path $options


