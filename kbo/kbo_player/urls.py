from django.urls import path
from . import views


urlpatterns = [
    path('',views.kbo_player_list,name='kbo_player_list'),
    path('kbo_player/<int:pk>',views.kbo_player_detail,name = 'kbo_player_detail'),
]