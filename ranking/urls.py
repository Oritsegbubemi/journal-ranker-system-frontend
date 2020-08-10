from django.urls import path
from . import views

urlpatterns = [
	path('card/', views.card, name='card'),
    path('rank/', views.rank, name='rank'),
    path('result/', views.result, name='result'),
    path('viewrank/<str:pk>/', views.viewrank, name='viewrank'),
    path('rank2/', views.rank2, name='rank2'),
    path('journals/', views.journals, name='journals'),
]

