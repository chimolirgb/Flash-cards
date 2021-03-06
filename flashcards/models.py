from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField 

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = CloudinaryField('image')
    bio = models.CharField(max_length=300)
    name = models.CharField(blank=True, max_length=120)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def profile(cls):
        profiles = cls.objects.all()
        return profiles

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def save_profile(self):
        self.user

    def __str__(self):
        return self.name

class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)

    def save_category(self):
        self.save()


class Card(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    posted = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ["-pk"]
    def save_card(self):
        self.save()

    def delete_card(self):
        self.delete()

    def __str__(self):
        return self.title
    



