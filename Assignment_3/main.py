# I have used the documentation of mongodb and python in help of doing in this assignment
# https://www.mongodb.com/resources/languages/python

import pymongo

def main():

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    create_databases(client)
    location_menu(client)

def location_menu(client):
    while True:
        print("\nChoose a location:")
        print("1) US")
        print("2) UK")
        print("3) Europe")
        print("0) Exit")

        location_choice = input("Enter your choice: ").strip()

        if location_choice == '1':
            display_data(client, "Database_US")
        elif location_choice == '2':
            display_data(client, "Database_UK")
        elif location_choice == '3':
            display_data(client, "Database_Europe")
        elif location_choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

def display_data(client, db_name):
    print(f"\nData from {db_name}:\n")

    # Access the selected location database
    db = client[db_name]

    # Display users
    print("Users (Username, Location, Subscription):")
    for user in db.users.find():
        print(f"{user.get('username')}, {user.get('location')}, {user.get('subscription')}")
    print("\n" + "-" * 50 + "\n")

    # Display global playlists
    print("Global Playlists (Name, Songs):")
    for playlist in db.global_playlists.find():
        print(f"{playlist.get('name')}: {', '.join(playlist.get('songs', []))}")
    print("\n" + "-" * 50 + "\n")

    # Display artists
    print("Artists (Name, Genre):")
    for artist in db.artists.find():
        print(f"{artist.get('name')}, {artist.get('genre')}")
    print("\n" + "-" * 50 + "\n")

    # Display albums
    print("Albums (Title, Artist, Release Year):")
    for album in db.albums.find():
        print(f"{album.get('title')}, {album.get('artist')}, {album.get('release_year')}")
    print("\n" + "-" * 50 + "\n")

    # Display songs
    print("Songs (Title, Artist, Duration):")
    for song in db.songs.find():
        print(f"{song.get('title')}, {song.get('artist')}, {song.get('duration')} seconds")
    print("\n" + "-" * 50 + "\n")

    # Display region-specific playlists
    print("Regional Playlists (Name, Songs):")
    for playlist in db.playlists.find():
        print(f"{playlist.get('name')}, {', '.join(playlist.get('songs', []))}")

    print("\n" + "*" * 50 + "\n")

def create_databases(client):
    # Defining global playlists that will be replicated across all location-specific databases
    global_playlists_data = [
        {"name": "Top 40", "songs": ["Song1", "Song2", "Song3"]},
        {"name": "Chill Hits", "songs": ["Song4", "Song5", "Song6"]},
        {"name": "Jazz Hits", "songs": ["Song4", "Song5", "Song6"]},
        {"name": "Classic Rock", "songs": ["Stairway to Heaven", "Money", "Bad Moon Rising"]},
        {"name": "80s Rock", "songs": ["Pour Some Sugar on Me", "Sultans of Swing"]},
        {"name": "Rock Hits", "songs": ["Pour Some Sugar on Me", "Money"]},
        {"name": "Pop Hits", "songs": ["No Tears Left to Cry", "Bad Guy", "Don't Start Now"]},
        {"name": "Dance Vibes", "songs": ["Don't Start Now", "Reiviluola"]},
    ]

    global_users_data = [
        {"username": "user1", "location": "Global", "subscription": "Premium"},
        {"username": "user_common", "location": "Global", "subscription": "Free"}
    ]

    # defining data for databases of each genre
    music_data = {
        "Database_UK": {
            "users": [
                {"username": "user_uk", "location": "UK", "subscription": "Premium"},
            ],
            "artists": [
                {"name": "Led Zeppelin", "genre": "Rock"},
                {"name": "Billie Eilish", "genre": "Pop"},
                {"name": "John Coltrane", "genre": "Jazz"},
                {"name": "Ariana Grande", "genre": "Pop"},
                {"name": "Pink Floyd", "genre": "Rock"},
                {"name": "The Beatles", "genre": "Rock/Pop"},  # Replicated
            ],
            "albums": [
                {"title": "Led Zeppelin IV", "artist": "Led Zeppelin", "release_year": 1971},
                {"title": "The Wall", "artist": "Pink Floyd", "release_year": 1979},
                {"title": "Sweetener", "artist": "Ariana Grande", "release_year": 2018},
                {"title": "A Love Supreme", "artist": "John Coltrane", "release_year": 1965},
                {"title": "Abbey Road", "artist": "The Beatles", "release_year": 1969},  # Replicated 
                
            ],
            "songs": [
                {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "duration": 482},
                {"title": "Money", "artist": "Pink Floyd", "duration": 354},
                {"title": "No Tears Left to Cry", "artist": "Ariana Grande", "duration": 205},
                {"title": "Giant Steps", "artist": "John Coltrane", "duration": 305},
                {"title": "Bad Guy", "artist": "Billie Eilish", "duration": 194},
                {"title": "Hey Jude", "artist": "The Beatles", "duration": 431},  # Replicated 
            ],
            "playlists": [
                {"name": "Mixed Hits UK", "songs": ["Stairway to Heaven", "Bad Guy", "No Tears Left to Cry"]},
            ],
        },
        "Database_US": {
            "users": [
                {"username": "user_us", "location": "US", "subscription": "Free"},
            ],
            "artists": [
                {"name": "Queen", "genre": "Rock"},
                {"name": "Dua Lipa", "genre": "Pop"},
                {"name": "Louis Armstrong", "genre": "Jazz"},
                {"name": "Def Leppard", "genre": "Rock"},
                {"name": "Glenn Miller", "genre": "Jazz"},
                {"name": "The Beatles", "genre": "Rock/Pop"},  # Replicated
            ],
            "albums": [
                {"title": "News of the World", "artist": "Queen", "release_year": 1977},
                {"title": "Future Nostalgia", "artist": "Dua Lipa", "release_year": 2020},
                {"title": "What a Wonderful World", "artist": "Louis Armstrong", "release_year": 1967},
                {"title": "Hysteria", "artist": "Def Leppard", "release_year": 1987},
                {"title": "Abbey Road", "artist": "The Beatles", "release_year": 1969},  # Replicated
            ],
            "songs": [
                {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354},
                {"title": "Don't Start Now", "artist": "Dua Lipa", "duration": 183},
                {"title": "What a Wonderful World", "artist": "Louis Armstrong", "duration": 141},
                {"title": "Pour Some Sugar on Me", "artist": "Def Leppard", "duration": 293},
                {"title": "In the Mood", "artist": "Glenn Miller", "duration": 198},
                {"title": "Hey Jude", "artist": "The Beatles", "duration": 431},  # Replicated
            ],
            "playlists": [
                {"name": "US Top Tracks", "songs": ["Bohemian Rhapsody", "Don't Start Now", "In the Mood"]},
            ],
        },
        "Database_Europe": {
            "users": [
                {"username": "user_eu", "location": "Europe", "subscription": "Premium"},
            ],
            "artists": [
                {"name": "Ella Fitzgerald", "genre": "Jazz"},
                {"name": "The Beatles", "genre": "Rock/Pop"},
                {"name": "Haloo Helsinki", "genre": "Pop"},
                {"name": "Frank Sinatra", "genre": "Jazz"},
                {"name": "CCR", "genre": "Rock"},
            ],
            "albums": [
                {"title": "Ella and Louis", "artist": "Ella Fitzgerald", "release_year": 1956},
                {"title": "Abbey Road", "artist": "The Beatles", "release_year": 1969},
                {"title": "Älä pelkää elämää", "artist": "Haloo Helsinki", "release_year": 2021},
                {"title": "Cycles", "artist": "Frank Sinatra", "release_year": 1968},
            ],
            "songs": [
                {"title": "Summertime", "artist": "Ella Fitzgerald", "duration": 210},
                {"title": "Hey Jude", "artist": "The Beatles", "duration": 431},
                {"title": "Reiviluola", "artist": "Haloo Helsinki", "duration": 219},
                {"title": "My Way", "artist": "Frank Sinatra", "duration": 542},
                {"title": "Bad Moon Rising", "artist": "CCR", "duration": 165},
            ],
            "playlists": [
                {"name": "European Classics", "songs": ["Summertime", "Hey Jude", "Bad Moon Rising"]},
            ],
        },
    }

    # Creating the regional databases and inserting data
    for db_name, data in music_data.items():
        db = client[db_name]

        # Insert global users and regional users if not already present
        if "users" not in db.list_collection_names():
            db.create_collection("users")
            db.users.insert_many(global_users_data)
            db.users.insert_many(data["users"])

        # Insert global playlists to all of the databases if not already exist
        if "global_playlists" not in db.list_collection_names():
            db.create_collection("global_playlists")
            db.global_playlists.insert_many(global_playlists_data)

        # Insert artists, albums, songs, and playlists if they don’t already exist
        if "artists" not in db.list_collection_names():
            db.create_collection("artists")
            db.artists.insert_many(data["artists"])

        if "albums" not in db.list_collection_names():
            db.create_collection("albums")
            db.albums.insert_many(data["albums"])

        if "songs" not in db.list_collection_names():
            db.create_collection("songs")
            db.songs.insert_many(data["songs"])

        if "playlists" not in db.list_collection_names():
            db.create_collection("playlists")
            db.playlists.insert_many(data["playlists"])

    print("Databases created and populated successfully.")

main()