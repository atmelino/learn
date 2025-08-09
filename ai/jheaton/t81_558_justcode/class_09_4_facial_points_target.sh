# conda activate stylegan3

# Train StyleGAN2  using 1 GPU.


# Download the pretrained model:
# wget nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/ffhq.pkl


# cmd = f"python /content/stylegan2-ada-pytorch/projector.py "\
# f"--save-video 0 --num-steps 1000 --outdir=out_target "\
# f"--target=cropped_target.png --network={NETWORK}"
# !{cmd}

code_path="../../../../local_data/packages/stylegan2-ada-pytorch/projector.py"
outdir_path="../../../../local_data/jheaton/class_09_4_facial_points"
data_path="../../../../local_data/jheaton/class_09_4_facial_points/cropped_target.png"
network_path="../../../../local_data/packages/stylegan2_pretrained/ffhq.pkl"

  

options="--save-video 0 --num-steps 1000"

python3 $code_path --outdir=$outdir_path --target=$data_path $options --network=$network_path



# NETWORK= "https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/ffhq.pkl"
