import calc_functions as cf

const_opr = ('+', '-', '/', '*')
while True:

    try:
        number_1 = int(input('Input number 1:  '))
    except ValueError:
        print('Please< enter only numbers!')
        continue

    operand = input('Input operation:  ')
    if operand not in const_opr:
        print('not valid operator')
        continue

    try:
        number_2 = int(input('Input number 2:  '))
    except ValueError:
        print('Please< enter only numbers!')
        continue

    if operand == '+':
        print(cf.c_sum(number_1, number_2))
    elif operand == '-':
        print(cf.c_diff(number_1, number_2))
    elif operand == '*':
        print(cf.c_mult(number_1, number_2))
    elif operand == '/' and number_2 == 0:
        print('division by zero is prohibited')
    else:
        print(cf.c_div(number_1, number_2))








