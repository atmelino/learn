# Train StyleGAN3-T for AFHQv2 using 8 GPUs.
# python train.py --outdir=~/training-runs --cfg=stylegan3-t --data=~/datasets/afhqv2-512x512.zip \
    # --gpus=8 --batch=32 --gamma=8.2 --mirror=1

# Fine-tune StyleGAN3-R for MetFaces-U using 1 GPU, starting from the pre-trained FFHQ-U pickle.
# python train.py --outdir=~/training-runs --cfg=stylegan3-r --data=~/datasets/metfacesu-1024x1024.zip \
    # --gpus=8 --batch=32 --gamma=6.6 --mirror=1 --kimg=5000 --snap=5 \
    # --resume=https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhqu-1024x1024.pkl

# Train StyleGAN2 for FFHQ at 1024x1024 resolution using 8 GPUs.
# python train.py --outdir=~/training-runs --cfg=stylegan2 --data=~/datasets/ffhq-1024x1024.zip \
    # --gpus=8 --batch=32 --gamma=10 --mirror=1 --aug=noaug

# Train StyleGAN2 for FFHQ at 256x256 resolution using 2 GPUs.
# python3 not_on_github/stylegan3/train.py --outdir=../../../../../sg3/training-runs --cfg=stylegan2 --data=../../../../../local_data/sg3/datasets/ffhq-256x256.zip \
#     --gpus=2 --batch=32 --gamma=10 --mirror=1 --aug=noaug


