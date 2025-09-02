prompt = f"\nPlease enter the topping you would like on your pizza."
prompt += f"\nEnter 'quit' to finish adding toppings on your pizza: "

# Conditional Test
"""toppings = ""

while toppings != "quit":
    toppings = input(prompt)

    if toppings != "quit":
        print(f"Adding {toppings} on your pizza!")
    
print(f"We will now proceed to making your pizza!")"""

# Active variable

"""active = True

while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping} on your pizza!")"""

# Break statement

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"Adding {topping} on your pizza!")

