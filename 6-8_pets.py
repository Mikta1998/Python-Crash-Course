pet_1 = {"name": "loki",
         "race": "dog"}

pet_2 = {"name": "johnny",
         "race": "parrot"}

pets = [pet_1, pet_2]

for pet in pets:
    print(f"{pet["name"]} is a {pet["race"]}!")