from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Category, Profile,Card
from .forms import ProfileForm,CardForm,UpdateUserProfileForm,UpdateUserForm,CategoryForm
from django.utils import timezone

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer

# Create your views here.

def welcome(request):
    categories = Category.objects.filter(user_id=request.user.id)
    return render(request, 'index.html', {"categories": categories})

# def post(request):
#     if request.method == 'POST':
#         form =CardForm(request.POST,request.FILES)

#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user.profile
#             post.save()
#         return redirect('/')
#     else:
#         form =CardForm()

#     return render(request,'post.html',{'form':form})



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
def profile(request,username):
 
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        # 'projects': projects,
    }
    return render(request, 'profile.html',params)



class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

def category(request, category):
    current_category = Category.objects.get(id=category)
    cards = Card.objects.filter(category_id=category)
    return render(request, 'category.html', {"category": current_category, "cards": cards})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category(category_name=form.cleaned_data.get('category_name'),
                        user=request.user)
            category.save()
            return redirect('welcome')
        else:
            return render(request, 'addcategory.html', {'form': form})
    else:
        form = CategoryForm()
        return render(request, 'addcategory.html', {'form': form})

def add_card(request, category):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = Card(title=form.cleaned_data.get('title'),
                        content=form.cleaned_data.get('content'),
                        category=Category.objects.get(id=category))
            card.save()
            return redirect('category', category=int(category))
        else:
            return render(request, 'post.html', {'form': form})
    else:
        form = CardForm()
        return render(request, 'post.html', {'form': form})



def delete_card(request, card):
    current_card=Card.objects.get(id=card)
    category=current_card.category
    current_card.delete()
    return redirect('category', category=category.id)

def edit_card(request, card):
    page_title = "Edit Card"
    editting_card = Card.objects.get(id=card)

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = Card.objects.get(id=card)
            card.title=form.cleaned_data.get('title')
            card.notes=form.cleaned_data.get('notes')
            card.date_updated = timezone.now()
            card.save()
            return redirect('category', category=card.category.id)
        else:
            return render(request, 'add-card.html', {'form': form, "page_title": page_title})
    else:
        form = CardForm(initial={'title': editting_card.title, 'notes': editting_card.notes})
        return render(request, 'add-card.html', {'form': form, "page_title": page_title})

def logout(request):
    logout(request)
    return redirect('login')
