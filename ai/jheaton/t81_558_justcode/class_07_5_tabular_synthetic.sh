

# wget https://raw.githubusercontent.com/Diyago/GAN-for-tabular-data/master/requirements.txt


wget https://raw.githubusercontent.com/Diyago/Tabular-data-generation/refs/heads/master/requirements.txt



conda create -y --name mytabgan python=3.10
conda activate mytabgan
pip install -r requirements.txt
pip install tabgan
pip install tensorflow
