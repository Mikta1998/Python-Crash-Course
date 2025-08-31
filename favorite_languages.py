favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

friends = ["phil", "sarah"]

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}! ")

"""language = favorite_languages["sarah"].title()

print(f"Sarah's favorite language is {language}")

point_value = favorite_languages.get("mikta", "No point value assigned.")
print(point_value)

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(name)
for language in favorite_languages.values():
    print(language)"""