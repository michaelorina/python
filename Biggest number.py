# Determine the biggest number between 2 numbers and display it an appropriate message

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if (a > b):
    print(f'{a} is greater than {b}')
elif (a == b):
    print("The numbers are equal")
else:
    print(f'{b} is greater than {a}')    