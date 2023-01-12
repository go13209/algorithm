number1 = int(input())
number2 = int(input())
if number1 > 0 and number2 > 0:
    print(1)
elif number1 < 0 and number2 > 0:
    print(2)
elif number1 < 0 and number2 < 0:
    print(3)
else:
    print(4)