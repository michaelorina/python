#You just opened an account that earns 2.1 interest per year. Dispay the amount you'll have over 1, 2, 3 years. Initial deposit is 45
#Use only 2 decimal places for each amount.

#My code before I watched the answer video

#initial_amount = 45
#amount_1 = initial_amount + (initial_amount * 0.021)
#amount_2 = amount_1 + (amount_1 * 0.021)
#amount_3 = amount_2 + (amount_2 * 0.021)

#print(f'The amount youll have in year 1 is {amount_1}. Year 2 is {amount_2}. Year 3 is {amount_3}.')

deposit = 45
interest_rate = 1.021

first_year = deposit * interest_rate
print(f'After first year you will have {first_year:.2f} in your acccount')

second_year = first_year * interest_rate
print(f'After first year you will have {second_year:.2f} in your acccount')

third_year = second_year * interest_rate
print(f'After first year you will have {third_year:.2f} in your acccount')