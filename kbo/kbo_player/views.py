
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Kboplayer,Comment
from .forms import PlayerForm,CommentForm



def kbo_player_list(request): #선수리스트
    kbo_player = Kboplayer.objects.all()
    return render(request,'kbo_player/kbo_list.html',{'players':kbo_player})

def kbo_player_detail(request,pk): #선수상세목록
    player_detail = Kboplayer.objects.get(pk=pk)
    return render(request,'kbo_player/kbo_detail_list.html',{'players_detail':player_detail})

def kbo_player_new(request): #새로운 선수 등록
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)

            player.created_date = timezone.now()
            player.update_date = timezone.now()
            player.save()
            return redirect('kbo_player_list')
    else:
        form = PlayerForm()
    return render(request,'kbo_player/kbo_new_player.html',{'form':form})



def kbo_player_edit(request,pk): #선수수정
    kbo_player = Kboplayer.objects.get(pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=kbo_player)
        if form.is_valid():
            kbo_player = form.save(commit=False)
            kbo_player.updated_date = timezone
            kbo_player.save()
            return  redirect('kbo_player_detail', pk = kbo_player.pk)
    else:
        form = PlayerForm(instance=kbo_player)
    return render(request,'kbo_player/kbo_new_player.html',{'form':form})

def kbo_player_remove(request,pk):
    kbo_player = Kboplayer.objects.get(pk=pk)
    kbo_player.delete()
    return redirect('kbo_player_list')


def add_comment_to_player(request,pk):
    kbo_player = Kboplayer.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.player_post = kbo_player
            comment.save()
            return redirect('kbo_player_detail',pk=kbo_player.pk)
    else:
        form = CommentForm()
    return render(request,'kbo_player/add_comment_to_player.html',{'form':form})

def comment_remove(request,pk):
    comment = Comment.objects.get(pk=pk)
    player_pk = comment.player_post.pk
    comment.delete()
    return redirect('kbo_player_detail',pk=player_pk)