requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping.title()}")

print(f"\nFinished making your pizza!")
