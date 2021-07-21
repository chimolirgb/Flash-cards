from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

        url(r'^create/profile$',views.create_profile, name='create-profile'),
        url(r'^profile/',views.profile, name='profile'),
        url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
        url(r'^api/profiles/$', views.ProfileList.as_view()),
        url('^$',views.welcome,name = 'welcome'),
        
        ]
