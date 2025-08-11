
# Resume Training StyleGAN3 for dogs at 256x256 resolution using 2 GPUs.
# Enter a snapshot file for resume

code_path="../../../../local_data/packages/stylegan3/train.py"
outdir_path="../../../../local_data/jheaton/class_07_2_train_gan/training-runs"
data_path="../../../../local_data/jheaton/class_07_2_train_gan/datasets/dogs-256x256.zip"

options="--cfg=stylegan2 --gpus=2 --batch=32 --gamma=10 --mirror=1 --aug=noaug --resume=../../../../local_data/jheaton/class_07_2_train_gan/training-runs/network-snapshot-003800.pkl"

python3 $code_path --outdir=$outdir_path --data=$data_path $options

        


