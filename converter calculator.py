def days_seconds():
    user_input = input("Enter Day (d) or Seconds (s): ")

    if user_input == "d":
        user_value = input("Enter days to be converted to Seconds: ")
        print("That is {} Seconds. ".format(int(user_value) * 24 * 60 * 60))

    if user_input == "s":
        user_value = input("Enter Seconds to be converted to days: ")
        print("That is {} Days. ".format(int(user_value) / 24 / 60 / 60))

def cels_fahr():
    user_input = input("Enter Celcius (c) or Farhaneit (f): ")

    if user_input == "c":
        user_value = input("Enter Celcius to be converted to Farhaneit: ")
        print("That is {} Farhaneit. ".format((int(user_value) * (9/5)) + 32))

    if user_input == "f":
        user_value = input("Enter Farhaneit to be converted to Celcius: ")
        print("That is {} Celcius. ".format((int(user_value) - 32) * (5/9)))

def miles_cent():
    user_input = input("Enter miles (m) or Centimeter (c): ")

    if user_input == "m":
        user_value = input("Enter miles to be converted to Centimeter: ")
        print("That is {} Centimeter. ".format(int(user_value) * 160934))

    if user_input == "c":
        user_value = input("Enter Centimeter to be converted to miles: ")
        print("That is {} miles. ".format(int(user_value) / 160934))        
days_seconds()
cels_fahr()
miles_cent()