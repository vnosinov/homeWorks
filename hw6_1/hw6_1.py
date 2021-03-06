import calc_functions as cf

OPERATORS = {
    '+': cf.c_sum,
    '-': cf.c_diff,
    '*': cf.c_mult,
    '/': cf.c_div,
}

while True:

    try:
        number_1 = int(input('Input number 1:  '))
    except ValueError:
        print('Please< enter only numbers!')
        continue

    operator = input('Input operation:  ')
    if operator not in OPERATORS:
        print('not valid operator')
        continue

    try:
        number_2 = int(input('Input number 2:  '))
    except ValueError:
        print('Please< enter only numbers!')
        continue

    print('result: ', OPERATORS[operator](number_1, number_2))
