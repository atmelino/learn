echo conda environment for this program:
echo conda activate stylegan3
echo Requires Nvidia GPU

my_URL="https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhq-1024x1024.pkl"

code_path="../../../../local_data/stylegan3/gen_images.py"
outdir_path="../../../../local_data/jheaton/class_07_1_gan_intro_sh"

mkdir $outdir_path

# python3 $code_path --network=$my_URL --outdir=./not_on_github/results --seeds=6600-6625


