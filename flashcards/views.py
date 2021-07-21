from django.shortcuts import render,redirect
from .forms import CardForm

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

def mycards(request):
    return render(request, 'cards.html')