import sys
sys.path.insert(0, "./not_on_github//stylegan3")
import torch
import dnnlib
import legacy





def expand_seed(seeds, vector_size):
    result = []

    for seed in seeds:
        rnd = np.random.RandomState(seed)
        result.append( rnd.randn(1, vector_size) )
    return result

my_URL="https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhq-1024x1024.pkl"

print(f'Loading networks from "{my_URL}"...')
device = torch.device('cuda')
with dnnlib.util.open_url(my_URL) as f:
    print("dnnlib.util.open_url",f)
    G = legacy.load_network_pkl(f)['G_ema'].to(device) # type: ignore




