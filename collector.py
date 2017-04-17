def update_list():
    with open('music.csv') as csvfile:
        to_split = csvfile.readlines()
        splitted = [line.split(" | ") for line in to_split]
        music_list = [((line[0].replace('\ufeff', ''), line[1]), (int(line[2]), line[3], line[4].replace('\n', ''))) for line in splitted]
        return(music_list)

def calculate_age(music_list):
    from datetime import date
    age = 0
    for main_tuple in music_list:
        year = int(main_tuple[1][0])
        current_year = date.today()
        current_year = int(current_year.year)
        age += current_year - year
    print("age of all albums : %i years" %age)

def find_by_genre(music_list):
    albums_list = []
    genre_not_in = True
    print("enter genre :")
    genre = input()
    for main_tuple in music_list:
        if genre.lower() == main_tuple[1][1].lower():
            artist = main_tuple[0][0]
            album_name = main_tuple[0][1]
            album = album_name + " made by " + artist
            albums_list.append(album)
            genre_not_in = False
    if genre_not_in == False:
        print("\n".join(albums_list))
    else:
        print("album not found")

def random_by_genre(music_list):
    import random
    albums_list = []
    genre_not_in = True
    print("enter genre :")
    genre = input()
    for main_tuple in music_list:
        if genre.lower() == main_tuple[1][1].lower():
            artist = main_tuple[0][0]
            album_name = main_tuple[0][1]
            album = album_name + " made by " + artist
            albums_list.append(album)
            genre_not_in = False
    if genre_not_in == False:
        print(random.choice(albums_list))
    else:
        print("album not found")

def find_by_letter(music_list):
    albums_list = []
    letter_not_in = True
    flag = True
    while flag:
        print("enter letter that is in album title :")
        album_title = input()
        if album_title != " ":
            flag = False
            for main_tuple in music_list:
                if album_title.lower() in main_tuple[0][1].lower():
                    album_name = main_tuple [0][1]
                    artist = main_tuple [0][0]
                    album = album_name + " made by " + artist
                    albums_list.append(album)
                    letter_not_in = False
            if letter_not_in == False:
                print("\n".join(albums_list))
            else:
                print("album not found")

def find_by_album(music_list):
    artists_list = []
    wrong_artist = True
    print("enter full album name :")
    album_name = input()
    for main_tuple in music_list:
        if album_name.lower() == main_tuple[0][1].lower():
            artist = main_tuple[0][0]
            artists_list.append(artist)
            wrong_artist = False
    if wrong_artist == False:
        print("\n".join(artists_list))
    else:
        print("artist not found ! ")

def find_by_year(music_list):
    albums_list = []
    wrong_year = True
    wrong_input = True
    while wrong_input:
        print("enter year of album:")
        year = input()
        if year.isdigit():
            for main_tuple in music_list:
                if year == str(main_tuple[1][0]):
                    author = main_tuple[0][0]
                    album_name = main_tuple[0][1]
                    album = album_name + " made by " + author + " in " + year
                    albums_list.append(album)
                    wrong_year = False
            if wrong_year == False:
                print("\n".join(albums_list))
            else:
                print("there is not album from %s" %year)
            wrong_input = False
        else:
            print("i don't think this is a year")

def find_by_artist(music_list):
    albums_list = []
    artist_found = False
    print("Enter name of artist:")
    artist = input()
    for main_tuple in  music_list:
        if artist.lower() == main_tuple[0][0].lower():
            author = main_tuple[0][0]
            album_name = main_tuple[0][1]
            year = str(main_tuple[1][0])
            album = album_name + " made by " + author + " in " + year
            albums_list.append(album)
            artist_found = True
    if artist_found == True:
        print("\n".join(albums_list))
    else:
        print("artist_found !")

def create_album():
    notcorrect = True
    print("Enter name of artist: ")
    artist = input()
    print("Enter name of album: ")
    album = input()
    while notcorrect:
        print("Enter year of release album: ")
        year = input()
        if year.isdigit():
            notcorrect = False
    print("Enter type of music: ")
    type_music = input()
    print("Enter time of album in format min:sec (for example 43:42): ")
    time = input()

    arguments = artist + ' | ' + album + ' | ' + year + ' | ' + type_music + ' | ' + time
    with open('music.csv', "a") as add_album:
        add_album.write(arguments + "\n")

def main():
    music_list = update_list()
    update_list()
    print("Welcome in CoolMusic, choose the action:\n")
    while True:
        print("\n1)add new album")
        print("2)find albums by artist")
        print("3)find albums by year")
        print("4)find musician by album")
        print("5)find albums by letter(s)")
        print("6)find albums by genre")
        print("7)calculate age of all albums")
        print("8)choose random album by genre")
        print("0)exit")
        action = input()
        if action == "1":
            create_album()
            music_list = update_list()
        elif action == "2":
            find_by_artist(music_list)
        elif action == "3":
            find_by_year(music_list)
        elif action == "4":
            find_by_album(music_list)
        elif action == "5":
            find_by_letter(music_list)
        elif action == "6":
            find_by_genre(music_list)
        elif action == "7":
            calculate_age(music_list)
        elif action == "8":
            random_by_genre(music_list)
        elif action == "0":
            exit()
        else:
            print("invalid sign!")



main()
