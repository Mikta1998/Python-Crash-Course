motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.insert(0, "kawasaki")
print(motorcycles)
motorcycles.append("honda")
print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)