from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    pass






class Card(models.Model):
    # user = models.ForeignKey('Profile', on_delete=models.CASCADE,related_name='projects')
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    posted = models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=50)

    class Meta:
        ordering = ["-pk"]
    def save_card(self):
        self.save()

    def delete_card(self):
        self.delete()

    def __str__(self):
        return self.title
    