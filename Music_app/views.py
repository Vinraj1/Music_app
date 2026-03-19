from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from . models import Song
import requests
import base64
from .services.deezer import search_songs
from django.http import JsonResponse

def index(request):
    songs = get_trending()

    for song in songs:
        deezer_data = search_songs(f"{song['title']} {song['artist']}")

        print("SEARCHING:", f"{song['title']} {song['artist']}")

        if deezer_data:
            best = deezer_data[0]
            song["preview"] = best.get("preview")
            song["cover"] = best.get("cover")
        else:
            song["preview"] = None

    return render(request, "index.html", {"songs": songs})

def upload_song(request):
    if request.method == "POST":
        title = request.POST.get("title")
        artist = request.POST.get("artist")
        image = request.FILES.get("image")
        audio_file = request.FILES.get("audio_file")
        audio_link = request.POST.get("audio_link")
        lyrics = request.POST.get("lyrics")
        duration = request.POST.get("duration")

        Song.objects.create(
            title=title,
            artist=artist,
            image=image,
            audio_file=audio_file,
            audio_link=audio_link,
            lyrics=lyrics,
            duration=duration
        )

        return redirect('/')

    return render(request,"upload_song.html")

def search(request):
    query = request.GET.get('q')

    songs = []
    if query:
        results = search_songs(query)

        songs = results

    return render(request, "search.html", {"songs": songs})
'''
def get_trending():

    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "geo.gettoptracks",   # ✅ India-specific
        "country": "india",
        "api_key": "a1dd591c4f90718c9b93d3472353b1aa",
        "format": "json"
    }

    res = requests.get(url, params=params)
    data = res.json()

    songs = []

    tracks = data.get("tracks", {}).get("track", [])

    for track in tracks[:12]:
        songs.append({
            "title": track.get("name"),
            "artist": track.get("artist", {}).get("name"),
        })

    return songs
'''

def get_trending():

    import requests

    url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "chart.gettoptracks",   # global
        "api_key": "a1dd591c4f90718c9b93d3472353b1aa",
        "format": "json"
    }

    res = requests.get(url, params=params)
    data = res.json()

    songs = []

    # 🔥 Indian artist keywords
    indian_keywords = [
        "arijit", "pritam", "shreya", "atif", "armaan",
        "badshah", "neha", "jubin", "darshan", "vishal",
        "anirudh", "sidhu", "kk", "sonu", "sunidhi"
    ]

    tracks = data.get("tracks", {}).get("track", [])

    # 🔥 loop through MORE tracks (important)
    for track in tracks:
        artist = track.get("artist", {}).get("name", "").lower()

        if any(k in artist for k in indian_keywords):
            songs.append({
                "title": track.get("name"),
                "artist": track.get("artist", {}).get("name"),
            })

        if len(songs) == 12:   # limit AFTER filtering
            break

    return songs