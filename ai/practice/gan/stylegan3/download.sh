# Download the flickrfaces dataset:
#
# 1. Create a directory for the data, for example:
# mkdir ../../../../../local_data/practice/test_sg3
#
# 2. Open a browser at
# https://drive.usercontent.google.com/download?id=16N0RV4fHI6joBuKbQAoG34V_cQk7vxSA&export=download
# Download the file named ffhq-dataset-v2.json into the abovec created directory.
#
# 3. Place the file ffhq-dataset-v2.json and the script named download_ffhq.py in the same directory.
#
# 4. Run the script:

flickrfaces_path="../../../../../local_data/practice/test_sg3"

cd $flickrfaces_path
python3 download_ffhq.py --json --images
