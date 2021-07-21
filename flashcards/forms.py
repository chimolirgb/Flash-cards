from django import forms
from .models import Profile,Project,Rating,Comment

class ProjectForm(forms.ModelForm):  
    class Meta:
        model = Project
        fields = ('title','content','category')