from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
  if request.method == 'POST':
    password = request.POST['password']
    username = request.POST['username']

    if password == request.POST['confirm-password']:
      try:
        user = User.objects.get(username=username)
        return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
      except User.DoesNotExist:
        user = User.objects.create_user(username, password)
        auth.login(request, user)
        return redirect('home')
    else:
      return render(request, 'accounts/signup.html', {'error': 'Passwords Must Math'})
  else:
    return render(request, 'accounts/signup.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'accounts/login.html', {'error': 'Username or Password is incorrect.'})

  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('home')
