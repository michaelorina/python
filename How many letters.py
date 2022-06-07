# Take two inputs, first and last name. Merge them with a space between and calculate the number of letters in your full name.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

name = f'{first_name} {last_name}'
print(len(name)-1)

# print(f'{first_name} {last_name}' + len(f'{first_name} + {last_name}'))