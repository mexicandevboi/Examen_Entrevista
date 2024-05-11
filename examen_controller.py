import json
import random

def get_albums():
    with open('albums.json') as file:
        return json.load(file)

def search_albums(search_query):
    results = []
    for album in get_albums():
        if search_query.lower() in album['Album'].lower() or search_query.lower() in album['Artista'].lower():
            results.append(album)

    # Return the search results if there are any or None if there are no results
    return results if results else None

def get_random_albums():
    albums = get_albums()
    visited_albums = [album for album in albums if album.get('Visitado') == 'False'] #Filter a list of albums that have not been visited
    non_nominated_albums = [album for album in visited_albums if album.get('Nominado') == 'False'] #From the list of non-visited albums, filter a list of albums that have not been nominated
    random_albums = random.sample(non_nominated_albums, min(4, len(non_nominated_albums))) #Select a random sample of 4 albums or less

    # Mark the displayed albums as nominated
    for album in random_albums:
        album['Nominado'] = True

    return random_albums