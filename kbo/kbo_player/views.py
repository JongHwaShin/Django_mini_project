
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Kboplayer
from .forms import PlayerForm


def kbo_player_list(request):
    kbo_player = Kboplayer.objects.all()
    return render(request,'kbo_player/kbo_list.html',{'players':kbo_player})

def kbo_player_detail(request,pk):
    player_detail = Kboplayer.objects.get(pk=pk)
    return render(request,'kbo_player/kbo_detail_list.html',{'players_detail':player_detail})

def kbo_player_new(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.created_date = timezone.now()
            player.save()
            return redirect('kbo_player_detail',pk = player.pk)
    else:
        form = PlayerForm()
    return render(request,'kbo_player/kbo_new_player.html',{'form':form})

