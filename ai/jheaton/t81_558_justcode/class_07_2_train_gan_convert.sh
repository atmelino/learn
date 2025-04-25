echo conda environment for this program:
echo conda activate stylegan3

mkdir ../../../../local_data/jheaton/class_07_2_train_gan
mkdir ../../../../local_data/jheaton/class_07_2_train_gan/data
mkdir ../../../../local_data/jheaton/class_07_2_train_gan/data/gan
mkdir ../../../../local_data/jheaton/class_07_2_train_gan/data/gan/images
mkdir ../../../../local_data/jheaton/class_07_2_train_gan/data/gan/dataset
mkdir ../../../../local_data/jheaton/class_07_2_train_gan/data/gan/images/circuit
mkdir ../../../../local_data/jheaton/class_07_2_train_gan/data/gan/dataset/circuit


# ../../../../local_data/jheaton

code_path="../../../../local_data/stylegan3/dataset_tool.py"
data_path="../../../../local_data/jheaton/class_07_2_train_gan/data/gan/images/circuit"
outdir_path="../../../../local_data/jheaton/class_07_2_train_gan/data/gan/dataset/circuit"

python3 $code_path  --source $data_path --dest $outdir_path 



# python3 not_on_github/stylegan2-ada-pytorch/dataset_tool.py \
# --source not_on_github/class_07_2_train_gan/data/gan/images/circuit \
# --dest not_on_github/class_07_2_train_gan/data/gan/dataset/circuit

