# Modify these to suit your needs
EXPERIMENTS = "/content/drive/MyDrive/data/gan/experiments"
DATA = "/content/drive/MyDrive/data/gan/dataset/circuit"
SNAP = '10'


# Build the command and run it
python3 not_on_github/stylegan2-ada-pytorch/train.py --snap={SNAP} --outdir {EXPERIMENTS} --data {DATA}


