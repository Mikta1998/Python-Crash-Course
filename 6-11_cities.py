cities = {
    "strumica": {"country": "macedonia",
                 "population": 50000},
    "windsbach": {"country": "germany",
                  "population": 5000},
}

for city, information in cities.items():
    print(f"Information about the following {city}:")
    print(f"The city is located in {information["country"]} and has an approximate population of {information["population"]} people.")