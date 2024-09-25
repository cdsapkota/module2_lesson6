def name_check(f_name, l_name):
    first_name_length = len(f_name)
    if first_name_length < 2:
        print("Error: Your first name needs to be at least 2 characters long.")
    
    last_name_length = len(l_name)
    if last_name_length < 2:
        print("Error: Your last name needs to be at least 2 characters long.")

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

name_check(first_name, last_name)