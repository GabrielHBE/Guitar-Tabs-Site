from . import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class SongForm(forms.ModelForm):

    tab = forms.FileField(widget=forms.FileInput(attrs={'songs':'/*',}))

    class Meta: 
        model = models.Song
        fields = ('song_name', 'song_author', 'yt_video', 'audio', 'tab', 'style')


class RegisterForm(UserCreationForm):
    pass


class ArtistForm(forms.ModelForm):

    class Meta: 
        model = models.Artist
        fields = ('name',)


    def clean(self):
        cleaned_data = self.cleaned_data

        name = cleaned_data.get('song_author')

        return super().clean()

class RegisterForm(UserCreationForm):
    pass