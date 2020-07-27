from django.urls import path
from . import views

urlpatterns = [
	path('card/', views.card, name='card'),
    path('rank/', views.rank, name='rank'),
    path('result/', views.result, name='result'),
    path('viewrank/', views.viewrank, name='viewrank'),
    path('ranking/', views.ranking2, name='ranking2'),
    #path('dragndrop/', views.dragndrop, name='dragndrop'),
    #path('download/', views.download, name='download'),
]

