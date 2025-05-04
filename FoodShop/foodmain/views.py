from django.shortcuts import render, redirect, HttpResponse
from .models import Food, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignupForm

# Create your views here.
def main(request):
    all_foods = Food.objects.all()
    return render(request, 'index.html', {'foods': all_foods})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login successful."))
            return redirect("home")
        else:
            messages.success(request, ("Error in login."))
            return redirect("login")
    else:
        return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, ('Logout successful.'))
    return redirect("home")

def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('Account is created successfully.'))
            return redirect('home')
        else:
            messages.error(request, ('Error in sign up.'))
            return render(request, "signup.html", {'form': form})
    else:
        form = SignupForm()
    
    return render(request, "signup.html", {'form': form})

def food(request, fd):
    food = Food.objects.get(id=fd)
    return render(request, "food.html", {'food': food})

def category(request, cat):
    cat = cat.replace('-',  '')
    #try:
    category = Category.objects.get(name=cat)
    foods = Food.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'foods': foods})
"""    except:
        return redirect('home')"""