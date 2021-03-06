import os


def recurs_dir(my_path):
    for i in os.listdir(my_path):
        if os.path.isfile(my_path+'/'+i):
            print(my_path+'/'+i)
        else:
            recurs_dir(my_path+'/'+i)


if __name__ == '__main__':
    my_path = '/home/vladimir/python'
    recurs_dir(my_path)
