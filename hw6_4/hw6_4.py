# проверка года на высокосность
while True:
    try:
        year = int(input('Input number: '))
    except ValueError:
        print('this is not a number')
        exit()

    if year % 4 != 0:
        print('this is a noy leap year')
    elif year % 100 == 0:
        if year % 400 == 0:
            print('this is a leap year')
        else:
            print('this is a not leap year')
    else:
        print('this is a leap year')





