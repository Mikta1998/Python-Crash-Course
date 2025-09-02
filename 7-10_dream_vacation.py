dream_vacation = {}

polling_active = True

while polling_active:
    name = input("Please enter your name? ")
    dream_place = input("if you could visit one place, which place would that be?")
    dream_vacation[name] = dream_place

    repeat = input(f"Would you like to let another person answer? (yes/no) ")

    if repeat == "no":
        polling_active = False

for name, dream_place in dream_vacation.items():
    print(f"{name.title()} would like to visit {dream_place}!")
    