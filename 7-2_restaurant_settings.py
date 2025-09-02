restaurant_reservation = int(input(f"How many people are in the group? "))

if restaurant_reservation > 8:
    print(f"You will have to wait for a table.")
else:
    print(f"Your table is ready. Please follow me!")