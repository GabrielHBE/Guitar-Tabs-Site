from home import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.index, name='create'),
    path('<author>/', views.index, name='author'),
    path('<author>/<song>/', views.index, name='song'),
]