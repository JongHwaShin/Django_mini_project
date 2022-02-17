from django import forms
from .models import Kboplayer,Comment

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Kboplayer
        fields = ('name','team','position','year_money','year','attack_or_attacked')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')