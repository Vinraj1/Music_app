import requests

def search_songs(query):
    url = "https://striveschool-api.herokuapp.com/api/deezer/search"

    try:
        response = requests.get(url, params={"q": query})

        # ✅ check if response is OK
        if response.status_code != 200:
            return []

        data = response.json()

    except Exception as e:
        print("DEEZEER ERROR:", e)
        return []

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