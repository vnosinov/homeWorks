def transform_str(str_in):
    str_tmp = ''
    result = ''

    for i in str_in:
        if not str.isnumeric(i):
            i = '*'+i+"*"
        str_tmp += i
    s = list(str_tmp.split('*'))
    s2 = s.pop(0)

    b = {s[i]: s[i + 1] for i in range(0, len(s), 2)}
    for key in b:
        result = result + key * int(b[key])
    return result


def file_processing(file_name):
    file_in = open(file_name, 'r')
    lines = file_in.readlines()
    file_in.close()
    file_out = open('output.txt', 'w')
    for i in range(len(lines)):
        if i != '':
            s = str(lines[i]).strip()
            out_str = transform_str(s)
            file_out.write(out_str + '\n')


if __name__ == '__main__':

    f = input('Input filename: ')
    file_processing(f)
