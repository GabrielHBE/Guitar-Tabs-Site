from . import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class SongForm(forms.ModelForm):

    tab = forms.FileField(widget=forms.FileInput(attrs={'accept':'/*',}))

    class Meta: 
        model = models.Song
        fields = ('song_name', 'song_author', 'yt_video', 'audio', 'tab', 'style')


    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('song_name')
        last_name = cleaned_data.get('song_author')

        if first_name==last_name:
            self.add_error('first_name',ValidationError('Os nomes não podem ser iguais',code='invalid1'))
            self.add_error('last_name',ValidationError('Os nomes não podem ser iguais',code='invalid2')) 

        return super().clean()


class RegisterForm(UserCreationForm):
    pass