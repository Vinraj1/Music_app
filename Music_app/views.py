from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from . models import Song

def index(request):
    paginator = Paginator(Song.objects.all().order_by('id'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

def upload_song():
    from django.shortcuts import render, redirect
from .models import Song

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

        return redirect("home")

    return render(request,"upload_song.html")