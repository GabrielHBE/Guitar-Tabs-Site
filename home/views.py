from django.shortcuts import render,get_object_or_404,redirect
from home.models import Song,Artist
from django.core.paginator import Paginator
from django.urls import reverse 
from home.forms import SongForm
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

    Artist = get_object_or_404(Song,pk=artist,show=True)

    context = {
        'contact':Artist,
        'title': Song.song_author
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


#list of songs by this artist
def songs(request, artist, song):

    artist = get_object_or_404(Artist.name, username=artist)

    song = get_object_or_404(Song.song_name, id=song, artist=artist)

    songs = Song.objects.filter(show=True).order_by('-id')
    paginator = Paginator(songs, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'artist': artist,
        'song': song,
        'title' : f'{Artist.name} - Songs',
        'page_obj': page_obj
    }

    return render(request, 'home/songs.html', context)

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


#Create tabs
def create(request):

    form_action = reverse('home:create')

    if request.method == 'POST':

        form = SongForm(request.POST,request.FILES)

        context = {
            'title':'Create contact',
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save() #salvar os dados na base de dados

            return redirect('home:index',contact_id=contact.pk)
        
        return render(
            request,
            'home/create.html',
            context
            )
    
    context = {
                'title':'Create contact',
                'form': SongForm(),
                'form_action': form_action,
            }
    
    return render(
            request,
            'home/create.html',
            context
            )