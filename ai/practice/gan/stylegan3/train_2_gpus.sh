# conda activate stylegan3

# Train StyleGAN2 for FFHQ at 256x256 resolution using 2 GPUs.


python3 not_on_github/stylegan3/train.py --outdir=../../../../../local_data/sg3/training-runs --cfg=stylegan2 --data=../../../../../local_data/sg3/datasets/ffhq-256x256.zip \
    --gpus=2 --batch=32 --gamma=10 --mirror=1 --aug=noaug



