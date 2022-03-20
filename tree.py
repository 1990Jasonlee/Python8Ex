import os

# def write_file(file_path, content):
#     fout = open(file_path, 'w')
#     fout.write(content)

def file(name, files):
    result = os.listdir(name)
    for item in result:
        path = os.path.join(name, result)
