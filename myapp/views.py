from django.shortcuts import render,redirect,HttpResponse
from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Registration successfull</h1>")
    f=RegisterForm()
    return render(request,'register.html',context={'form':f})
