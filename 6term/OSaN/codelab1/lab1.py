import os
import pathlib

pathlib.Path().absolute()

matchFiles = []


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            if f.find('myfile') == 0:
                matchFiles.append(os.path.realpath(f))


def merge(filesLst):
    result = open("result.txt", "w+")
    for f in filesLst:
        with open(f, mode='rb') as file:
            result.write(file.read(256).decode('utf8'))
    result.close()


if __name__ == "__main__":
    # print("Введите директорию")
    # dirname = input()
    list_files(str(pathlib.Path().absolute()))
    print(matchFiles)
    merge(matchFiles)
