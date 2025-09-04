"""pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)"""


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet("hamster","willy")
describe_pet("dog","loki")

#KEYWORD ARGUMENTS
describe_pet(pet_name="johnny", animal_type="parrot")