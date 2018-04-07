from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
  return render(request, 'products/home.html')

@login_required
def create(request):
  if request.method == 'POST':
    title = request.POST['title']
    body = request.POST['body']
    url = request.POST['url']
    icon = request.FILES['icon']
    image = request.FILES['image']

    if title and body and url and icon and image:
      product = Product()
      product.title = title
      product.body = body

      if url.startswith('http://') or url.startswith('https://'):
        product.url = url
      else:
        product.url = 'http://' + url

      product.icon = request.FILES['icon']
      product.image = request.FILES['image']
      product.pub_date = timezone.datetime.now()
      product.hunter = request.user
      product.save()
      return redirect('home')

    else:
      return render(request, 'products/create.html', {'error': 'All fields are required.'})

  else:
    return render(request, 'products/create.html')