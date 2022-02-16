from django.shortcuts import render, get_object_or_404
from .models import Kboplayer


def kbo_player_list(request):
    kbo_player = Kboplayer.objects.all()
    return render(request,'kbo_player/kbo_list.html',{'players':kbo_player})

def kbo_player_detail(request,pk):
    player_detail = Kboplayer.objects.get(pk=pk)
    return render(request,'kbo_player/kbo_detail_list.html',{'players_detail':player_detail})

# Create your views here.
