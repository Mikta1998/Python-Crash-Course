def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("filip", "timov",
                             age=26,
                             hobby="kickboxing",
                             course_of_study="AI")


print(user_profile)

for key, value in user_profile.items():
    print(key, value)