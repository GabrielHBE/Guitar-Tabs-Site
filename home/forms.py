from .models import *
from django import forms # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore



from django import forms
from .models import Song, Artist

from django import forms
from .models import Song, Artist

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_name', 'song_author', 'yt_video', 'audio', 'tab', 'style', 'instrument']

    def __init__(self, *args, **kwargs):
        artist_queryset = kwargs.pop('artist_queryset', Artist.objects.none())
        super().__init__(*args, **kwargs)
        self.fields['song_author'].queryset = artist_queryset

class ArtistForm(forms.ModelForm):

    class Meta: 
        model = Artist
        fields = ('name',)


    def clean(self):
        return super().clean()


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True)  # Pode ser mantido, pois o campo `username` é obrigatório

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
