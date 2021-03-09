import os


def recurs_dir(my_path):
    result = []
    for i in os.listdir(my_path):
        path = os.path.join(my_path, i)
        if not os.path.isdir(path):
            result.append(path)
        else:
            result += recurs_dir(path)
    return result


if __name__ == '__main__':
    my_path = '/home/vladimir/python'
    my_list = recurs_dir(my_path)
    for item in my_list:
        print(item)
