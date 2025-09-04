age = int(input(f"Please enter your age: "))

while age != 0:
    if age < 3:
        print(f"The ticket is free!")
    elif age >= 3 and age < 12:
        print(f"The ticket is $10.")
    elif age >= 12:
        print(f"The ticket is $15.")
        


