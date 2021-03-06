
def get_acronym(s):
    x = s.split()
    res = ''
    for e in x:
        res += e[0]
    return res


if __name__ == '__main__':
    my_str = 'very Cool phrase dvf Fjj'
    print(get_acronym(my_str).upper())
