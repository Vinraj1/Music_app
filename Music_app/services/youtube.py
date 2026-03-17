import requests

API_KEY = "AIzaSyAAg2NoMlZKOrI_KUvun9F3RBKMRr_MIU4"

def get_video(query):
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "key": API_KEY,
        "maxResults": 3,
        "type": "video"
    }

    res = requests.get(url, params=params)
    data = res.json()

    if "items" not in data:
        return None

    for item in data["items"]:
        video_id = item["id"].get("videoId")
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"

    return None

def get_video_for_song(song):
    if song.video_url:
        return song.video_url  # already saved

    video = get_video(song.title)

    if video:
        song.video_url = video
        song.save()

    return video