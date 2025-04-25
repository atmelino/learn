# Using stylegan3 for this module because stylegan2 did not work on my systems
echo conda environment for this program:
echo conda activate stylegan3




# Modify these to suit your needs
code_path="../../../../local_data/stylegan3/train.py"
data_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-32x32_small.zip"
outdir_path="../../../../../local_data/practice/stylegan3_ffhq_small/training-runs"
options="--cfg=stylegan2 --gpus=2 --batch=8 --gamma=10 --mirror=1 --aug=noaug --kimg=200 --snap=1"

python3 $code_path --outdir=$outdir_path --data=$data_path $options





code_path="../../../../local_data/stylegan3/train.py"
data_path="../../../../local_data/jheaton/class_07_2_train_gan/data/gan/dataset/circuit"
outdir_path="../../../../local_data/jheaton/class_07_2_train_gan/output"

OUTPUT="not_on_github/stylegan2-ada-pytorch/data/gan/experiments"
SNAP='10'
python3 $code_path  --cfg=stylegan2 --snap 10 --outdir not_on_github/class_07_2_train_gan/data/gan/output --data not_on_github/class_07_2_train_gan/data/gan/dataset/circuit










# Build the command and run it
# python3 not_on_github/stylegan2-ada-pytorch/train.py --snap={SNAP} --outdir {EXPERIMENTS} --data {DATA}
# python3 not_on_github/stylegan2-ada-pytorch/train.py --snap 10 --outdir not_on_github/class_07_2_train_gan/data/gan/output --data not_on_github/class_07_2_train_gan/data/gan/dataset/circuit

# python3 not_on_github/stylegan3/train.py --cfg=stylegan2 --snap 10 --outdir not_on_github/class_07_2_train_gan/data/gan/output --data not_on_github/class_07_2_train_gan/data/gan/dataset/circuit




