# conda environment for this program:
# conda activate ?


import torch
import dnnlib
import legacy
import PIL.Image
import numpy as np
import imageio
from tqdm.notebook import tqdm

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = "../../../../local_data/tfds/"
PACKAGES_PATH="../../../../local_data/packages/"
SHAPE_PRED_PATH="../../../../local_data/packages/shape_predictor/"
OUTPUT_PATH = BASE_PATH+"class_09_4_facial_points/"
OUT_SOURCE_PATH=OUTPUT_PATH+"out_source/"
OUT_TARGET_PATH=OUTPUT_PATH+"out_target/"

lvec1 = np.load(OUT_SOURCE_PATH+'projected_w.npz')['w']
lvec2 = np.load(OUT_TARGET_PATH+'projected_w.npz')['w']

network_pkl = "https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/ffhq.pkl"
device = torch.device('cuda')
with dnnlib.util.open_url(network_pkl) as fp:
    G = legacy.load_network_pkl(fp)['G_ema'].requires_grad_(False).to(device)

diff = lvec2 - lvec1
step = diff / STEPS
current = lvec1.copy()
target_uint8 = np.array([1024,1024,3], dtype=np.uint8)

video = imageio.get_writer(OUTPUT_PATH+'movie.mp4', mode='I', fps=FPS,codec='libx264', bitrate='16M')

for j in tqdm(range(STEPS)):
    z = torch.from_numpy(current).to(device)
    synth_image = G.synthesis(z, noise_mode='const')
    synth_image = (synth_image + 1) * (255/2)
    synth_image = synth_image.permute(0, 2, 3, 1).clamp(0, 255)\
    .to(torch.uint8)[0].cpu().numpy()
    repeat = FREEZE_STEPS if j==0 or j==(STEPS-1) else 1

    for i in range(repeat):
        video.append_data(synth_image)
    current = current + step

video.close()


