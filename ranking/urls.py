from django.urls import path
from . import views

urlpatterns = [
	path('card/', views.card, name='card'),
    path('rank/', views.rank, name='rank'),
    path('result/', views.result, name='result'),
    path('viewrank/<str:pk>/', views.viewrank, name='viewrank'),
    path('deletecard/<str:pk>/', views.deletecard, name='deletecard'),
    path('journals/', views.journals, name='journals')
]

