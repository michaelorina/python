#Determine the sum of digits for 3 digits number. The program should display the following format for example 254: 2+5+4=11

#method 1

number = int(input('Enter  a 3 digit number: '))

last_digit = number%10
middle_digit = number//10%10
first_digit = number//100

sum = first_digit + middle_digit + last_digit

print(f'{number}: {first_digit} + {middle_digit} + {last_digit} = {sum}')

#method 2

number = int(input('Enter  a 3 digit number: '))

initial_number = number
last_digit = number%10
number = number//10
middle_digit = number%10
first_digit = number//10

sum = first_digit + middle_digit + last_digit

print(f'{initial_number}: {first_digit} + {middle_digit} + {last_digit} = {sum}')