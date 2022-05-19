# Write a program that converts days in seconds, Celcius in Farenheit, miles in centimeters

days = int(input("Enter number of days: "))
seconds = days * 86400
print(f'{days} days equals to {seconds} seconds.')

celcius = int(input("Enter temperature in Celcius: "))
Far = celcius * 1.8 + 32
print (f'{celcius} celcius equals to {Far} Farenheit.')

miles = float(input("Enter distance in miles: "))
cm = miles * 160934
print (f'{miles} miles equals {cm} cm. ')