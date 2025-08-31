person = 26

if person < 2:
    print(f"The person is a baby.")
elif person >= 2 and person < 4:
    print(f"The person is a toddler")
elif person >= 4 and person < 13:
    print(f"The person is a kid.")
elif person >= 13 and person < 20:
    print(f"The person is a teenager.")
elif person >= 20 and person < 65:
    print(f"The person is an adult.")
elif person >= 65:
    print(f"The person is an elder.")