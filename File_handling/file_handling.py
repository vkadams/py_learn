# creating a file - approach 1
# file = open(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\myfile1.txt','w')
# file.write("Hello World\nThis is my first python file")
# file.close()

# approach 2 -- using with keyword
# with open(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\myfile2.txt','w') as file:
#     file.write("Hello World \nThis is my second python file")
#     file.close()

# Appending data into existing file.
# file = open(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\myfile1.txt','a')
# file.write("\nThis line is appended to the file")
# file.close()

# reading data from file
'''read()-- reads entire data as text format
readline()-- reads single line
readlines()-- reads all the lines into a list format
'''
# fileopen = open(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\myfile1.txt','r')
# content = fileopen.read()
# #print(content)
# fileopen.seek(0)
# #print(fileopen.readline())
# fileopen.seek(0)
# print(fileopen.readlines()) #-- output is list
# fileopen.close()

# renaming the file
# we need to import os module
# import os
# os.rename(r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\myfile1.txt',r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\myfile1_renamed.txt')
# print('File renamed')

# deleting the file
import os
file = r'C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\myfiles\myfile1.txt'
# first check if file exists
if os.path.exists(file):
    os.remove(file)
else:
    print('File does not exist')