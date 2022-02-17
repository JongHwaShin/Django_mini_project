from django import forms
from .models import Kboplayer

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Kboplayer
        fields = ('name','team','position','year_money','year','attack_or_attacked')