from django.shortcuts import render,redirect
from .forms import CardForm

# Create your views here.
def post(request):
    if request.method == 'POST':
        form =CardForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            submit = form.save(commit=False)
            submit.user = request.user.profile
            submit.save()
        return redirect('/')
    else:
        form =CardForm()

    return render(request,'post.html',{'form':form})