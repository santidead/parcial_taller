
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    
    path('players/', views.list_jugadores, name="list_jugador"),
    path('players/create/', views.jugador_create, name="jugador_create"),
    path('players/inserted/', views.add_jugador, name="add_jugador"),
    path('players/delete/<int:id>', views.delete_jugador, name="delete_jugador"),
    path('players/edit/<int:id>', views.edit_jugador, name="edit_jugador"),
    path('players/update/', views.update_jugador, name="update_jugador"),
]