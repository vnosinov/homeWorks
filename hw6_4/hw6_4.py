# проверка года на высокосность
while True:
    try:
        year = int(input('Input number: '))
    except ValueError:
        print('this is not a number')
        continue

    # if year % 4 != 0:
    #     print('this is a noy leap year')
    # elif year % 100 == 0:
    #     if year % 400 == 0:
    #         print('this is a leap year')
    #     else:
    #         print('this is a not leap year')
    # else:
    #     print('this is a leap year')

    if year % 4 != 0:
        print('this is a noy leap year', '1')
    elif year % 100 == 0 and year % 400 != 0:
        print('this is a noy leap year', '2')
    else:
        print('this is leap year', '3')
