users = {
    "aenstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },

    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"Username: {username.title()}")
    print(f"\tFirst Name: {user_info["first"].title()}")
    print(f"\tLast Name: {user_info["last"].title()}")
    print(f"\tLocation: {user_info["location"].title()}")
    print(f"\n")