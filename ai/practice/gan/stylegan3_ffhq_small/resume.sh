echo conda activate stylegan3

                                                                                                                                                                        
# Train StyleGAN2 for FFHQ at 32x32 resolution using 2 GPU.

code_path="../../../../../local_data/stylegan3/train.py"
outdir_path="../../../../../local_data/practice/stylegan3_ffhq_small/training-runs"
data_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-32x32_small.zip"
options="--cfg=stylegan2 --gpus=2 --batch=8 --gamma=10 --mirror=1 --aug=noaug  --snap=1 --resume=../../../../../local_data/practice/stylegan3_ffhq_small/training-runs/00011-stylegan2-ffhq-32x32_small-gpus2-batch8-gamma10/network-snapshot-000200.pkl"

python3 $code_path --outdir=$outdir_path --data=$data_path $options

