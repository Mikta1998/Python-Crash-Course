cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
print("\n")

cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))                     #sorted function only temporarily sorts the list

print("\nHere is the original list again:")
print(cars)

print("\n")
cars.reverse()
print(cars)

print(len(cars))
