from django.urls import path
from . import views


urlpatterns = [
    path('',views.kbo_player_list,name='kbo_player_list'),
    path('player/kbo_money_list',views.kbo_money_list,name = 'kbo_money_list'),
    path('player/<int:pk>',views.kbo_player_detail,name = 'kbo_player_detail'),
    path('player/new/',views.kbo_player_new,name= 'kbo_player_new'),
    path('player/<int:pk>/edit',views.kbo_player_edit,name='kbo_player_edit'),
    path('player/<int:pk>/remove',views.kbo_player_remove,name='kbo_player_remove'),
    path('player/<int:pk>/comment/',views.add_comment_to_player,name='add_comment_to_player'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('player/kbo_batter_list/',views.kbo_batter_list,name='kbo_batter_list'),
]