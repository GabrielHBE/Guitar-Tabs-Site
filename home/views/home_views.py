from django.shortcuts import render,get_object_or_404
from home.models import Song,Artist
from django.core.paginator import Paginator

# Create your views here.

#Some random songs
def index(request):

    song = Song.objects.filter(show=True).order_by('-song_name')
    paginator = Paginator(song, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Home',
        'page_obj':page_obj,
    }

    return render(request,'home/index.html',context)


#A single artist
def artist(request,artist):

    Artist_ = get_object_or_404(Artist,pk=artist,show=True)

    songs = Song.objects.filter(song_author=Artist_,show=True).order_by('-song_name')
    paginator = Paginator(songs, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'Artist':Artist_,
        'title': Artist_.name,
        'page_obj': page_obj
    }
    
    return render(
        request,
        'home/artist.html',
        context
        )


#List of all artists
def artists(request):

    artists = Artist.objects.filter(show=True).order_by('-name')
    paginator = Paginator(artists, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'artists':Artist,
        'title': 'Artists',
        'page_obj': page_obj
    }

    return render(
        request,
        'home/artists.html',
        context
        )


#A single song by this artist
def song(request, artist, song):

    artist = get_object_or_404(Artist.name, username=artist)

    song = get_object_or_404(Song.song_name, id=song, artist=artist)

    context = {
        'artist': artist,
        'song': song,
        'title' : f'{Artist.name} - {Song.song_name}'
    }

    return render(request, 'home/song.html', context)

