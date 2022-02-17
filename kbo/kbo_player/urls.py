from django.urls import path
from . import views


urlpatterns = [
    path('',views.kbo_player_list,name='kbo_player_list'),
    path('player/<int:pk>',views.kbo_player_detail,name = 'kbo_player_detail'),
    path('player/new/',views.kbo_player_new,name= 'kbo_player_new'),
    path('player/<int:pk>/edit',views.kbo_player_edit,name='kbo_player_edit'),
    path('player/<int:pk>/remove',views.kbo_player_remove,name='kbo_player_remove'),
]