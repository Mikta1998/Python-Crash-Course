sandwich_orders = ["hamburger", "cheeseburger", "chickenburger", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []

print(f"The restaurant has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Sandwich being made: {sandwich}")
    finished_sandwiches.append(sandwich)

print("Sandwiches finished")
print("Finished sandwiches ready for delivery: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())


