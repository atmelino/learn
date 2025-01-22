# Modify these to suit your needs
OUTPUT="not_on_github/stylegan2-ada-pytorch/data/gan/experiments"
DATA="not_on_github/stylegan2-ada-pytorch/data/gan/dataset/circuit"
SNAP='10'


# Build the command and run it
# python3 not_on_github/stylegan2-ada-pytorch/train.py --snap={SNAP} --outdir {EXPERIMENTS} --data {DATA}


# python3 not_on_github/stylegan2-ada-pytorch/train.py --snap 10 --outdir not_on_github/class_07_2_train_gan/data/gan/output --data not_on_github/class_07_2_train_gan/data/gan/dataset/circuit
# python3 not_on_github/stylegan3/train.py --cfg=stylegan2 --snap 10 --outdir not_on_github/class_07_2_train_gan/data/gan/output --data not_on_github/class_07_2_train_gan/data/gan/dataset/circuit




python3 not_on_github/stylegan3/train.py  --gpus=2 --outdir=~/sg3/output/ --cfg=stylegan2 --data=~/sg3/data --gpus=2 --batch=32 --gamma=10 --mirror=1 --aug=noaug