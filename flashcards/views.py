from django.shortcuts import render,redirect
from .forms import CardForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from .forms import ProfileForm
from decouple import config,Csv
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer

# Create your views here.
def post(request):
    if request.method == 'POST':
        form =CardForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
        return redirect('mycards')
    else:
        form =CardForm()

    return render(request,'post.html',{'form':form})





# Create your views here.

def welcome(request):
    return render(request, 'index.html')



@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('Index')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
   
    
    return render(request,'profile.html')



class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


def logout(request):
    logout(request)
    return redirect('login')
