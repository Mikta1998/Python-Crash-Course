def sandwich_toppings(*toppings):
    print(f"\nSummary of your order:")
    for topping in toppings:
        print(f"Adding {topping} to your sandwich.")

sandwich_toppings("salami","cheese","ketchup")
sandwich_toppings("cheese","mayonnaise","steak")
