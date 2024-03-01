import os
import os.path

# path="."
# basename = os.path.basename(path)
# print("basename="+basename)
# dirname=os.path.dirname(path)
# print("dirname="+dirname)
print("path of current file="+__file__)
# print(__file__) 

#find the basename and dirname of the path
basename=os.path.basename(__file__)
dirname=os.path.dirname(__file__)
print('basename of the file: ', basename)
print('dirname of the file: ', dirname)




