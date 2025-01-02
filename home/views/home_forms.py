from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse 
from home.forms import SongForm,ArtistForm
from home.models import Song,Artist
# Create your views here.


#Create tabs
from home.forms import SongForm, ArtistForm
from home.models import Song, Artist

def create_tabs(request):
    form_action = reverse('home:create_tabs')

    if not request.user.is_authenticated:
        return redirect('home:login')

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, artist_queryset=Artist.objects.filter(user=request.user.username))

        context = {
            'title': 'Create Song',
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.user = request.user.username
            new_song.save()

            return redirect('home:index')

        return render(
            request,
            'home/create_song.html',
            context
        )

    context = {
        'title': 'Create Song',
        'form': SongForm(artist_queryset=Artist.objects.filter(user=request.user.username)),
        'form_action': form_action,
    }

    return render(
        request,
        'home/create_song.html',
        context
    )


def create_artist(request):
    form_action = reverse('home:create_artist')

    if not request.user.is_authenticated:
        return redirect('home:login')

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)

        context = {
            'title': 'Create Artist',
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            new_artist = form.save(commit=False)
            new_artist.user = request.user.username  
            new_artist.save() 

            return redirect('home:index')

        return render(
            request,
            'home/create_artist.html',
            context
        )

    context = {
        'title': 'Create Artist',
        'form': ArtistForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'home/create_artist.html',
        context
    )


