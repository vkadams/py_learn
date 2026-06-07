import os
import shutil

# writing to file (creates new if not exists, overwritest if exists)
def write_file(file_name, content):
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(content)
    print(f'File written to {file_name}')

# appending data into existing file
def append_to_file(file_name, content):
    with open(file_name, mode='a', encoding='utf-8') as f:
        f.write(content)
    print(f'File written to {file_name}')

# reading text file
def read_file(file_name, mode='all'):
    with open(file_name, mode='r', encoding='utf-8') as f:
        if mode == 'all':
            return f.read()
        elif mode == 'line':
            return f.readline()
        elif mode == 'lines':
            return f.readlines()
        else:
            raise ValueError(f'Invalid mode: {mode}')

# renaming a file
def rename_file(file_name, new_file_name):
    os.rename(file_name, new_file_name)
    print(f'File renamed to {new_file_name}')

# deleting a file
def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print('File deleted')
    else:
        print('File does not exist')



