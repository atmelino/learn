
# Resume Training StyleGAN3 for FFHQ at 256x256 resolution using 2 GPUs.
# Enter a snapshot file for resume

code_path="../../../../../local_data/stylegan3/train.py"
outdir_path="../../../../../local_data/practice/stylegan3_ffhq/training-runs"
data_path="../../../../../local_data/practice/stylegan3_ffhq/datasets/ffhq-256x256.zip"
options="--cfg=stylegan2 --gpus=2 --batch=32 --gamma=10 --mirror=1 --aug=noaug --resume=../../../../../stylegan3_ffhq/pkl/network-snapshot-003800.pkl"

python3 $code_path --outdir=$outdir_path --data=$data_path $options

        


