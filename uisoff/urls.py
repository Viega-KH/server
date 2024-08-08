from django.urls import path
from .views import (
    home, about, leader, new, 
    newdet, contactsite, contactmessage,
    homeselekt, tablesite, clubs, libraryviews, newad
)


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('office/', leader, name='leader'),
    path('news/', new, name='news'),
    path('news/ad/', newad, name='newad'),
    path('new/<int:id>/', newdet, name='newdet'),
    path('table/', tablesite, name='tablesite'),
    path('contact/', contactsite, name='contactsite'),
    path('contact/message/', contactmessage, name='contactmessage'),
    path('home/select/', homeselekt, name='homeselekt'),
    path('clubs/', clubs, name='clubs'),
    path('library/', libraryviews, name='library'),
]
