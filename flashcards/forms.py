from django import forms
from .models import Card, Profile

class CardForm(forms.ModelForm):  
    class Meta:
        model = Card
        fields = ('title','content','category')