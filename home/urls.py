from home import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('tabs/', views.index, name='index'),

    path('tabs/create_tabs/', views.create_tabs, name='create_tabs'),
    path('tabs/create_artist/', views.create_artist, name='create_artist'),
    path('tabs/artists/', views.artists, name='artists'),
    path('tabs/artists/<str:artist>/songs/', views.artist, name='artist'),
    path('tabs/artists/<str:artist>/songs/<str:song>/', views.song, name='song'),

    #user
    path('user/create/',views.register, name='register'),
    path('user/login/',views.login_view, name='login'),
    path('user/logout/',views.logout_view, name='logout'),
    path('user/update/',views.user_update, name='user_update'),
]