favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

friends = ["phil", "sarah", "antoine"]

for name in friends:
    if name in favorite_languages.keys():
        print(f"{name}, thank you for taking part in the poll!")
    else:
        print(f"{name}, please take part in the poll!")