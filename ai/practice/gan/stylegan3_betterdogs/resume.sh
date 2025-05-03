# Use stylegan3 conda environment
echo conda environment for this program:
echo conda activate stylegan3

                                                                                                                                                                        
# Resume training
code_path="../../../../../local_data/stylegan3/train.py"
data_path="../../../../../local_data/practice/stylegan3_betterdogs/datasets/dogs-256x256.zip"
outdir_path="../../../../../local_data/practice/stylegan3_betterdogs/output"
options1="--cfg=stylegan2 --gpus=2 --batch=8 --gamma=10 --mirror=1 --aug=noaug --kimg=200 --snap=1"
options2=" --resume=../../../../../local_data/practice/stylegan3_betterdogs/output/00005-stylegan2-dogs-32x32-gpus2-batch8-gamma10/network-snapshot-000096.pkl"
options=$options1$options2


python3 $code_path --outdir=$outdir_path --data=$data_path $options

