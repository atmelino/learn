
# https://github.com/NVlabs/stylegan3

# !git clone https://github.com/NVlabs/stylegan3.git
# !pip install ninja

echo Requires Nvidia GPU

my_URL="https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhq-1024x1024.pkl"


python3 ./not_on_github/stylegan3/gen_images.py --network=$my_URL --outdir=./not_on_github/results --seeds=6600-6625


