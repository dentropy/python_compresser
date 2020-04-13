#!/usr/bin/env python
import os
import zipfile

beginning_text = '''
import os
import zipfile

# http://www.codecodex.com/wiki/Read_a_file_into_a_byte_array#Python
def write_bytes(write_bytes_where, mah_bytes):
    f = open(write_bytes_where, 'wb')
    f.write(mah_bytes)
    f.close()

# https://stackoverflow.com/questions/3451111/unzipping-files-in-python
def unzip_file(file_path, output_path):
    with zipfile.ZipFile(file_path, 'r') as tyler_perry:
        tyler_perry.extractall(output_path)
'''


end_text = '''
write_bytes("mah_bytes.zip", mah_bytes)
unzip_file("mah_bytes.zip", "./unzipped_files")
os.remove("unzipped_files/Python.zip")
'''


# https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
    # Maybe use cwd = os.getcwd()

# https://stackoverflow.com/questions/12092527/python-write-bytes-to-file
def get_bytes_from_file(filename):  
    return open(filename, "rb").read()  

# http://www.codecodex.com/wiki/Read_a_file_into_a_byte_array#Python
def write_bytes(write_bytes_where, mah_bytes):
    f = open(write_bytes_where, 'wb')
    f.write(mah_bytes)
    f.close()

# https://stackoverflow.com/questions/3451111/unzipping-files-in-python
def unzip_file(file_path, output_path):
    with zipfile.ZipFile(file_path, 'r') as tyler_perry:
        tyler_perry.extractall(output_path)

if __name__ == '__main__':
    # https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory#5137509
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = "."
    print(dir_path)
    # The next four lines are from
    # https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(dir_path, zipf)
    zipf.close()
    print('All files zipped successfully!')  
    some_bytes = get_bytes_from_file("Python.zip") 
    with open("supermeta.py", 'a') as out:
        out.write(beginning_text + '\n')
        out.write("mah_bytes = " + str(some_bytes) + "\n")
        out.write(end_text + '\n')
    os.remove("Python.zip")

## Peach Pie is from https://ccsearch.creativecommons.org/photos/fe32017c-df1b-455c-9784-0f9b3a141717