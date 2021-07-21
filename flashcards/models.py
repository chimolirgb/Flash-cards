from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q


# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
