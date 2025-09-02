responses = {}

polling_active = True

while polling_active:
    name = input(f"\nWhat is your name? ")
    response = input(f"Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input(f"Would you like to let another person respond? (yes/no) ")

    if repeat == "no":
        polling_active = False

for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")