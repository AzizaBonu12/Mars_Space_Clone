from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render("Success")
        else:
            return render("Error")
    else:
        form = UserForm()
    return render(request, 'register.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render("Success")
        else:
            return render("Error")
    else:
        form = LoginForm()
    return render(request, 'register.html', {'form':form})


def admin(request):
    return render(request, 'admin.html')




