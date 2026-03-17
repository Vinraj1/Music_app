from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from . models import Song
import requests
import base64
from .services.deezer import search_songs
from .services.youtube import get_video
from django.http import JsonResponse


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

def search(request):
    query = request.GET.get('q')

    songs = []
    if query:
        results = search_songs(query)

        for song in results:
            video = get_video(f"{song['title']} {song['artist']}")
            song['video'] = video

        songs = results

    return render(request, "search.html", {"songs": songs})

def get_trending():
    url = "http://ws.audioscrobbler.com/2.0/"
    
    params = {
        "method": "chart.gettoptracks",
        "api_key": "YOUR_LASTFM_KEY",
        "format": "json"
    }

    res = requests.get(url, params=params)
    return res.json()

def get_video_api(request):
    query = request.GET.get("q")

    video = get_video(query)

    return JsonResponse({
        "video": video
    })