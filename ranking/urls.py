from django.urls import path
from . import views

urlpatterns = [
	path('card/', views.card, name='card'),
    path('rank1/', views.rank1, name='rank1'),
    path('rank2/', views.rank2, name='rank2'),
    path('result/', views.result, name='result'),
    path('viewrank/<str:pk>/', views.viewrank, name='viewrank'),
    path('deletecard/<str:pk>/', views.deletecard, name='deletecard'),
    path('journals/', views.journals, name='journals')
]

