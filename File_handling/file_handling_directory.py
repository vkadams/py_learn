# creating a directory
import os
#os.makedirs(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\new-folder')

# check if directory exist or not
folder_loc = r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\new-folder'
# if os.path.exists(folder_loc):
#     print('Directory exists')
# else:
#     print('Directory does not exist')

# renaming the directory
#os.rename(folder_loc,r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\new-folder-renamed')

# removing the directory - empty directory
# os.rmdir(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\removed')

# removing the directory - has files
import shutil
#shutil.rmtree(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\new-folder-renamed')

# get current working directory
print(os.getcwd())