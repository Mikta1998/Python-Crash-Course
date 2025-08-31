person_1 = {"first_name": "filip", "last_name": "timov", "city": "strumica", "age": 26}
person_2 = {"first_name": "goran", "last_name": "tomovski", "city": "strumica", "age": 27}
person_3 = {"first_name": "filip", "last_name": "gjorgiev", "city": "strumica", "age": 28}

people = [person_1, person_2, person_3]

for person in people:
    print(f"{person["first_name"].title()} {person["last_name"].title()} comes from {person["city"].title()} and is {person["age"]} years old.")
