from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('^/cards/$',views.post,name = 'post'),
    path(r'^create/profile/$',views.create_profile, name='create-profile'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path(r'^api/profiles/$', views.ProfileList.as_view()),
  


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


