requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping.title()}")
    print(f"\nFinished making your pizza!")
else:
    print(f"Are you sure you want a plain pizza?")
