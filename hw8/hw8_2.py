

def divisions(n):
    return [i for i in range(1, n+1) if n % i == 0]


if __name__ == '__main__':
    number = int(input('ввод: '))
    print('результат: ', divisions(number))
