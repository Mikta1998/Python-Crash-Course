current_users = ["legolas", "ezio", "war", "edward", "MIKTA"]
check_users = []
new_users = ["mikta", "edward", "fury", "aedwulf", "lorthran"]


for user in current_users:
    lowercase_user = user.lower()
    check_users.append(lowercase_user)

print(check_users)

for user in new_users:
    if user in current_users or user in check_users:
        print(f"That username is taken. Please choose another one!")
    else:
        print(f"Welcome back {user}!")

