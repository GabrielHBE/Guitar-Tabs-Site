from home import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('tabs/create/', views.create, name='create'),
    path('tabs/artists/', views.artists, name='artists'),
    path('tabs/artists/<str:artist>/', views.artist, name='artist'),
    path('tabs/artists/<str:artist>/songs/', views.songs, name='songs'),
    path('tabs/artists/<str:artist>/songs/<str:song>/', views.song, name='song'),
]