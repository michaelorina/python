def age_program():
    seconds_or_years = input("Give me Seconds (s) or years (y)")

    if seconds_or_years == "s":
        user_value = input("Enter the number of Seconds you've lived: ")
        print("You have lived for {} years".format(int(user_value)/60/60/24/365))
    elif seconds_or_years == "y":
        user_value = input("Enter the number of Years you've lived: ")
        print("You've lived for {} seconds".format(int(user_value)*60*60*24*365))
    else:
        print("Enter vlaues y or s")

age_program()