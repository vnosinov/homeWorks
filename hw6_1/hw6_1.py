while True:
    try:
        number_1 = int(input('Input number 1:  '))
        number_2 = int(input('Input number 2:  '))
    except ValueError:
        print('Please< enter only numbers!')
        exit()
    const_opr = ('+', '-', '/', '*')
    operand = input('Input operation:  ')
    if operand in const_opr:
        if operand == '+':
            print(number_1, '+', number_2, '=', number_1 + number_2)
        elif operand == '-':
            print(number_1, '-', number_2, '=', number_1 - number_2)
        elif operand == '*':
            print(number_1, '*', number_2, '=', number_1 * number_2)
        elif operand == '/' and number_2 == 0:
            print('division by zero is prohibited')
        else:
            print(number_1, '/', number_2, '=', number_1 / number_2)
    else:
        print('not valid operator')
