from django.db import models

# Create your models here.

class Style(models.Model):

    #Corrigir o erro do plural
    class Meta:
        verbose_name = 'Style'
        verbose_name_plural = 'Styles'

    name = models.CharField(max_length=50)
    show = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class Instrument(models.Model):

    #Corrigir o erro do plural
    class Meta:
        verbose_name = 'Instrument'
        verbose_name_plural = 'Instruments'

    name = models.CharField(max_length=50)
    show = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
  
class Artist(models.Model):

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    name = models.CharField(max_length=50)
    show = models.BooleanField(default=True)
    user = models.CharField(max_length=150,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    

class Song(models.Model):
    song_name = models.CharField(max_length=50)
    song_author = models.ForeignKey(Artist,on_delete=models.SET_NULL,null=True)
    show = models.BooleanField(default=True)
    yt_video = models.CharField(max_length=255, null=True, blank=True)
    audio = models.FileField(upload_to='Songs/', null=True, blank=True)
    tab = models.FileField(upload_to='Tabs/',null=True,blank=True)
    user = models.CharField(max_length=150,null=True,blank=True)
    style = models.ForeignKey(Style,on_delete=models.SET_NULL,blank=True,null=True)
    instrument = models.ForeignKey(Instrument,on_delete=models.SET_NULL,blank=True,null=True)

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self) -> str:
        return f'{self.song_name} {self.song_author}'