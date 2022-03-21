import os

# def write_file(file_path, content):
#     fout = open(file_path, 'w')
#     fout.write(content)

def file(name, files):
    #list all
    result = os.listdir(name)

    #check all in path and write in file
    for item in result:
        path = os.path.join(name, item)
        if os.path.isfile(path):
            files.write(path)
        else:
            file(path, files)