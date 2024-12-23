from home import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),

    path('tabs/create_tabs/', views.create_tabs, name='create_tabs'),
    path('tabs/create_artist/', views.create_artist, name='create_artist'),
    #path('tabs/create_style/', views.create_style, name='create_style'),
    path('tabs/artists/', views.artists, name='artists'),
    path('tabs/artists/<str:artist>/songs/', views.artist, name='artist'),
    path('tabs/artists/<str:artist>/songs/<str:song>/', views.song, name='song'),
]