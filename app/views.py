from django.contrib import messages
from django.shortcuts import render

from app.forms import SignUpForm

# Create your views here.

def home(request):
  return render(request, 'app/index.html')

def register(request):
  if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully')
            fm.save()
  else:
        fm = SignUpForm()
    
  return render(request, 'app/register.html', {'form':fm})

def login(request):
  return render(request, 'app/login.html')

def logout(request):
  pass
