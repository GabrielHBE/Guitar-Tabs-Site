from django.shortcuts import render,get_object_or_404,redirect
from home.models import Song,Artist
from django.core.paginator import Paginator
from django.urls import reverse 
from home.forms import SongForm
# Create your views here.


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