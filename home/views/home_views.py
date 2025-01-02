from django.shortcuts import render,get_object_or_404,redirect
from home.models import Song,Artist
from django.core.paginator import Paginator
from home.funcs import *

# Create your views here.

#Some random songs
def index(request):

    user_name = request.user.username

    if request.user.is_authenticated:

        song = Song.objects.filter(show=True,user=user_name).order_by('-song_name')
        paginator = Paginator(song, 10)  # Show 10 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'title': 'Home',
            'page_obj':page_obj,
        }

        return render(request,'home/index.html',context)

    return redirect('home:login')


#A single artist
def artist(request,artist):

    user_name = request.user.username
        
    if request.user.is_authenticated:


        Artist_ = get_object_or_404(Artist,pk=artist,show=True)

        songs = Song.objects.filter(song_author=Artist_,show=True,user=user_name).order_by('-song_name')
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
    
    return redirect('home:login')


#List of all artists
def artists(request):
    if not request.user.is_authenticated:
        return redirect('home:login')

    user_name = request.user.username

    # Filtrar artistas criados pelo usuário autenticado
    artists = Artist.objects.filter(show=True, user=user_name).order_by('-name')

    paginator = Paginator(artists, 10)  # Paginação com 10 artistas por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'artists': artists,  # Passa o queryset filtrado
        'title': 'Artists',
        'page_obj': page_obj,  # Objeto da página atual
    }

    return render(request, 'home/artists.html', context)


#A single song by this artist
def song(request, artist, song):
        
    if request.user.is_authenticated:

        artist_obj = get_object_or_404(Artist, id=artist)

        song_obj = get_object_or_404(Song, id=song, song_author=artist_obj)


        context = {
            'artist': artist_obj,
            'song': song_obj,
            'title' : f'{artist_obj.name} - {song_obj.song_name}',
            'tabs': song_obj.tab
        }

        return render(request, 'home/song.html', context)
    
    return redirect('home:login')