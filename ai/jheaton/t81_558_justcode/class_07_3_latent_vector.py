# Use conda stylegan3 environment
print("conda environment for this program:")
print("conda activate stylegan3")

import sys
sys.path.insert(0, "../../../../local_data/stylegan3")
import pickle
import os
import numpy as np
import PIL.Image
from IPython.display import Image
import matplotlib.pyplot as plt
import IPython.display
import torch
import dnnlib
import legacy

print("class_07_3_latent_vector")

outputdir="../../../../local_data/jheaton/class_07_3_latent_vector"
os.makedirs(outputdir, exist_ok=True)


def seed2vec(G, seed):
    return np.random.RandomState(seed).randn(1, G.z_dim)

def display_image(image):
    plt.axis('off')
    plt.imshow(image)
    plt.show()

def generate_image(G, z, truncation_psi):
    print("generate_image 1 called")
    # Render images for dlatents initialized from random seeds.
    Gs_kwargs = {
        'output_transform': dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True),
        'randomize_noise': False
    }
    if truncation_psi is not None:
        Gs_kwargs['truncation_psi'] = truncation_psi
    label = np.zeros([1] + G.input_shapes[1][1:])
    # [minibatch, height, width, channel]
    images = G.run(z, label, **G_kwargs)
    return images[0]

def get_label(G, device, class_idx):
    label = torch.zeros([1, G.c_dim], device=device)
    if G.c_dim != 0:
        if class_idx is None:
            ctx.fail(
                'Must specify class label with --class when using a conditional network'
            )
        label[:, class_idx] = 1
    else:
        if class_idx is not None:
            print (
                'warn: --class=lbl ignored when running on an unconditional network'
            )
    return label

def generate_image(device, G, z, truncation_psi=1.0, noise_mode='const', class_idx=None):
    print("generate_image 2 called")
    z = torch.from_numpy(z).to(device)
    label = get_label(G, device, class_idx)
    img = G(z, label, truncation_psi=truncation_psi, noise_mode=noise_mode)
    img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
    return PIL.Image.fromarray(img[0].cpu().numpy(), 'RGB')

my_URL="https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhq-1024x1024.pkl"

print('Loading networks from "%s"...' % my_URL)
device = torch.device('cuda')
with dnnlib.util.open_url(my_URL) as fp:
    print("dnnlib.util.open_url",fp)
    G = legacy.load_network_pkl(fp)['G_ema'].requires_grad_(False).to(device)

# Choose your own starting and ending seed.
SEED_FROM = 4020
SEED_TO = 4023
# Generate the images for the seeds.
for i in range(SEED_FROM, SEED_TO):
    print(f"Seed {i}")
    z = seed2vec(G, i)
    img = generate_image(device, G, z)
    display_image(img)
    filenumber=str(i).zfill(2)
    filename=f'frame-part1_'+filenumber+'.png'
    filepath=outputdir + "/" +filename
    print(filepath)
    img.save(filepath)


START_SEED = 4022
current = seed2vec(G, START_SEED)
# img = generate_image(device, G, current)
# SCALE = 0.5
# display_image(img)

EXPLORE_SIZE = 25
explore = []
for i in range(EXPLORE_SIZE):
    explore.append( np.random.rand(1, 512) - 0.5 )

# HIDE OUTPUT 1
# Choose the direction to move. Choose -1 for the initial iteration.

MOVE_DIRECTION = -1
# SCALE = 0.5
if MOVE_DIRECTION >=0:
    current = current + explore[MOVE_DIRECTION]
for i, mv in enumerate(explore):
    print(f"Direction {i}")
    z = current + mv
    img = generate_image(device, G, z)
    display_image(img)
    filenumber=str(i).zfill(2)
    filename=f'frame-part2_'+filenumber+'.png'
    filepath=outputdir + "/" +filename
    print(filepath)
    img.save(filepath)






