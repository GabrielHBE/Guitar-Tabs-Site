from django.db import models

# Create your models here.

class Category(models.Model):

    #Corrigir o erro do plural
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class Song(models.Model):
    song_name = models.CharField(max_length=50)
    song_author = models.CharField(max_length=50,blank=True)
    show = models.BooleanField(default=True)
    yt_video = models.CharField(max_length=255, null=True, blank=True)
    audio = models.FileField(upload_to='Audios/', null=True, blank=True)
    tab = models.FileField(blank=True,upload_to='Tab_files/')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.song_name} {self.song_author}'