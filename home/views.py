from django.shortcuts import render
from home.models import Song
from django.core.paginator import Paginator

# Create your views here.

def index(request):

    song = Song.objects.filter(show=True).order_by('-id')
    paginator = Paginator(song, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Home',
        'page_obj':page_obj,
    }

    return render(request,'home/index.html',context)

