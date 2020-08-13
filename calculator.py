def calculate():   
    operator = input('''Please enter:
    + for addition
    - for substraction
    * for multiplication
    / for division
    ** for power
    % for modulo
    ''')

    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    if operator == '+':
        print('{} + {} = '.format(num1,num2), num1 + num2)
    elif operator == '-':
        print('{} - {} = '.format(num1,num2), num1 - num2)
    elif operator == '*':
        print('{} * {} = '.format(num1,num2), num1 * num2)
    elif operator == '/':
        print('{} / {} = '.format(num1,num2), num1 / num2)
    elif operator == '**':
        print('{} ** {} = '.format(num1,num2), num1 ** num2)
    elif operator == '%':
        print('{} % {} = '.format(num1,num2), num1 % num2)
    else:
        print('You entered an invalid operator')
    again()

def again():
    calc_again = input('''Would you like use the calculator again?
    Type capital Y for yes and capital N for no: ''')
    if calc_again == 'Y':
        calculate()
    elif calc_again == 'N':
        print('See you soon!')
    else:
        again()
        
calculate()