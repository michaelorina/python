# Enter the price of a meal at a restaurant. Determine the tax paid for that meal at a tax rate of 
# your choice and tip at the rate 10% of the meal amount without the tax.
# Display meal price, tax, tip and Grand total on different lines in a user friendly format.

price = int(input('Enter the price of the meal: '))

tax = price * 0.16
tip = price * 0.1
meal_price = price + tax + tip

print('The price plus additional cost is as Follows\n\n*------------------------------*\n')
print(f'Meal price:{price}\nTax:{tax}\nTip:{tip}\nGrand Total:{meal_price}\n')