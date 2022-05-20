#Create a program that will...
#Create a variable that will hold a "magic number" between 1 and 10
#Tell the user to pick a number between 1 and 10
#If the user picks the magic number, tell them they have won
#Else, tell them to run the program again

magic_number = 7

user_input = int(input("Pick a number between 1 and 10: "))

if magic_number == user_input:
    print("You have won! ")

else:
    print("Run the program again. ")