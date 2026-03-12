from django.db import models

# Create your models here.
class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField(upload_to = "media/")
    audio_file = models.FileField(upload_to = "media/")
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    lyrics=models.TextField(blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def get_audio_url(self):
        if self.audio_file:
            return self.audio_file.url.replace('/media/media/', '/media/')
        return ""

    def get_image_url(self):
        if self.image:
            return self.image.url.replace('/media/media/', '/media/')
        return ""

    def __str__(self):
        return self.title
