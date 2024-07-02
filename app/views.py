from app.forms import SignInForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
  return render(request, 'app/index.html')

def register(request):
  if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully')
            fm.save()
            return redirect('login')
  else:
        fm = SignUpForm()
    
  return render(request, 'app/register.html', {'form':fm})

def logIn(request):
  if request.method == "POST":
     fm = SignInForm(request, data=request.POST)
     if fm.is_valid():
        user = fm.get_user()
        login(request, user)
        return redirect('home')
  else:
        fm = SignInForm()
  return render(request, 'app/login.html', {'fm':fm})

def logOut(request):
  logout(request)
  messages.success(request, 'You have been disconnected')
  return redirect('home')
