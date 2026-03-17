from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from . models import Song
import requests
import base64

def index(request):
    paginator = Paginator(Song.objects.all().order_by('id'), 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

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

CLIENT_ID = "9c3ba12d930c4f2aa551844484f39264"
CLIENT_SECRET = "89b8c8a5446e4a72abf30f177a54f854"


def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"

    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}"
    }

    data = {
        "grant_type": "client_credentials"
    }

    result = requests.post(url, headers=headers, data=data)
    json_result = result.json()

    return json_result.get("access_token")

def search_spotify(request):
    query = request.GET.get("q")

    if not query:
        return render(request, "search.html")

    token = get_spotify_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=10"

    response = requests.get(url, headers=headers)
    data = response.json()

    songs = []

    for item in data["tracks"]["items"]:
        songs.append({
            "title": item["name"],
            "artist": item["artists"][0]["name"],
            "image": item["album"]["images"][0]["url"],
            "preview": item["preview_url"]
        })

    return render(request, "search.html", {"songs": songs})