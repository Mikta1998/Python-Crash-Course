"""pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

print(f"You ordered a {pizza["crust"]}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")"""

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size} pizza with the following toppings:")
    for toppings in toppings:
        print(toppings)

