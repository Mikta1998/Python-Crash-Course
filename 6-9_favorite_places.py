favorite_places = {
    "mikta": ["strumica", "bairo", "belasica"],
    "bradr": ["strumica", "solun"]
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")