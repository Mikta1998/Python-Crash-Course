def make_album(artist_name, album_title, number_of_songs = None):#
    if number_of_songs:
        return {"artist name": artist_name, "album title": album_title, "number of songs": number_of_songs}
    else:
        return {"artist name": artist_name, "album title": album_title}


while True:
    print(f"Please enter your name, the name of your album and number of songs if you have any")
    print(f"\nPress 'q' at any time to quit")

    name = input("Please enter your name: ")
    if name == "q":
        break

    title = input(f"Please enter the name of your album: ")
    if title == "q":
        break

    songs = input("Please enter the number of songs (or press Enter to skip): ")
    if songs:
        songs = int(songs)

    profile = make_album(name, title, songs)
    print(profile)


