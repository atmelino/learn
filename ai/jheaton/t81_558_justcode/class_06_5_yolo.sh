echo conda environment for this program:
echo conda activate vision

code_path="../../../../local_data/yolov5/detect.py"  
data_path="../../../../local_data/jheaton/images"

python3 $code_path --weights yolov5s.pt --img 1024 --conf 0.25 --source $data_path