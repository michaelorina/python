# Determine how much change you need to provide if a shopper pays with cash at a checkout machine. Input the total to pay and the amount paid by the shopper.
# The machine should return as few coins as possible. Consider it is loaded with 1c, 5c, 10c, 25c, 50c and 1$.
# ex: for a total of $17.12 shopper paid 20$ and received back 2*$1, 1*50c, 1*10c, 0*5c, 3*1c

to_pay = float(input("Enter amount to pay: "))
total = int(input("Total paid: "))

change = (total - to_pay) * 100

c_1c = 1
c_5c = 5
c_10c = 10
c_25c = 25
c_50c = 50
c_1d = 100

print(f'{change//c_1d} x 1$')
change = change % c_1d

print(f'{change//c_50c} x 50c')
change = change % c_50c

print(f'{change//c_10c} x 10c')
change = change % c_10c

print(f'{change//c_5c} x 5c')
change = change % c_5c

print(f'{change} x 1c')