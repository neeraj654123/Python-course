import os

filename ='practice.txt'

if os.path.exists(filename):
    print("File exists")
else:
    print("File does not exists")
    fh =open(filename,'xt')
    fh.write("Some content")
    fh.close()