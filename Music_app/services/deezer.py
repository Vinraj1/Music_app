import requests

def search_songs(query):
    url = "https://striveschool-api.herokuapp.com/api/deezer/search"
    
    params = {
        "q": query
    }

    response = requests.get(url, params=params)
    data = response.json()

    songs = []
    for item in data.get('data', []):
        songs.append({
            "title": item['title'],
            "artist": item['artist']['name'],
            "album": item['album']['title'],
            "cover": item['album']['cover_medium'],
            "preview": item['preview']
        })

    return songs