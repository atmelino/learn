echo conda activate stylegan3

# Train StyleGAN2 for FFHQ at 256x256 resolution using 1 GPU.

# code_path="../../../../../local_data/stylegan3/train.py"                                                                                                              
# outdir_path="../../../../../local_data/practice/stylegan3_ffhq_small/training-runs"                                                                                   
# data_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-256x256_small.zip"                                                                   
# options="--cfg=stylegan2 --gpus=1 --batch=32 --gamma=10 --mirror=1 --aug=noaug --kimg=200"                                                                            
                                                                                                                                                                        
# python3 $code_path --outdir=$outdir_path --data=$data_path $options                                                                                                   
                                                                                                                                                                        
                                                                                                                                                                        
# Train StyleGAN2 for FFHQ at 128x128 resolution using 1 GPU.                                                                                                           
                                                                                                                                                                        
# code_path="../../../../../local_data/stylegan3/train.py"                                                                                                              
# outdir_path="../../../../../local_data/practice/stylegan3_ffhq_small/training-runs"                                                                                   
# data_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-128x128_small.zip"                                                                   
# options="--cfg=stylegan2 --gpus=1 --batch=32 --gamma=10 --mirror=1 --aug=noaug --kimg=200"                                                                            
                                                                                                                                                                        
# python3 $code_path --outdir=$outdir_path --data=$data_path $options                                                                                                   
                                                                                                                                                                        
                                                                                                                                                                        
# Train StyleGAN2 for FFHQ at 64x64 resolution using 2 GPU.                                                                                                             
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Train StyleGAN2 for FFHQ at 32x32 resolution using 2 GPU.

code_path="../../../../../local_data/stylegan3/train.py"
outdir_path="../../../../../local_data/practice/stylegan3_ffhq_small/training-runs"
data_path="../../../../../local_data/practice/stylegan3_ffhq_small/datasets/ffhq-32x32_small.zip"
options="--cfg=stylegan2 --gpus=2 --batch=8 --gamma=10 --mirror=1 --aug=noaug --kimg=200 --snap=1"

python3 $code_path --outdir=$outdir_path --data=$data_path $options

