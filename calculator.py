number1 = input('Enter the frist number: ')
num1 = int(number1)
sign = input('Enter an operator (+, -, *, /): ')
number2 = input('Enter the second number: ')
num2 = int(number2)
if sign =='+':
    print('your result is' + str(num1 +num2))
elif sign =='-':
    print('your result is' + str(num1 - num2))
elif sign =='*':
    print('your result is' + str(num1 * num2))
elif sign == "/":
    print('your result is' + str(num1 / num2))
else:
    print('please enter + , - , * or /')