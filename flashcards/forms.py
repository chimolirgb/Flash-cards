from django import forms

from .models import Card

class CardForm(forms.ModelForm):  
    class Meta:
        model = Card
        fields = ('title','content','category')

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

