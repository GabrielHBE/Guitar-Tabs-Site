from django.shortcuts import render,get_object_or_404
from home.models import Song,Artist
from django.core.paginator import Paginator
from home.funcs import *

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

    artist_obj = get_object_or_404(Artist, id=artist)

    song_obj = get_object_or_404(Song, id=song, song_author=artist_obj)

    pdf_path = song_obj.tab

    # Caminho da pasta de saída para as imagens
    output_folder = os.path.join('media', 'images', artist_obj.name, song_obj.song_name)

    # Criar a pasta de saída se não existir
    os.makedirs(output_folder, exist_ok=True)

    # Chamar a função para converter o PDF em imagens
    pdf_to_images(pdf_path, output_folder)

    # Listar as imagens geradas
    images = [f"/media/images/{artist_obj.name}/{song_obj.song_name}/{img}" for img in os.listdir(output_folder) if img.endswith(".png")]

    context = {
        'artist': artist_obj,
        'song': song_obj,
        'title' : f'{artist_obj.name} - {song_obj.song_name}',
        'tabs': images
    }

    return render(request, 'home/song.html', context)