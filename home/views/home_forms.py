from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse 
from home.forms import SongForm,ArtistForm
# Create your views here.


#Create tabs
def create_tabs(request):

    form_action = reverse('home:create_tabs')

    if request.method == 'POST':

        form = SongForm(request.POST,request.FILES)

        context = {
            'title':'Create Song',
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save() #salvar os dados na base de dados

            return redirect('home:index')
        
        return render(
            request,
            'home/create_song.html',
            context
            )
    
    context = {
                'title':'Create Song',
                'form': SongForm(),
                'form_action': form_action,
            }
    
    return render(
            request,
            'home/create_song.html',
            context
            )


def create_artist(request):

    form_action = reverse('home:create_artist')

    if request.method == 'POST':

        form = ArtistForm(request.POST,request.FILES)

        context = {
            'title':'Create Artist',
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save() #salvar os dados na base de dados

            return redirect('home:index')
        
        return render(
            request,
            'home/create_artist.html',
            context
            )
    
    context = {
                'title':'Create Artist',
                'form': ArtistForm(),
                'form_action': form_action,
            }
    
    return render(
            request,
            'home/create_artist.html',
            context
            )