from django.http import HttpResponse
from django.shortcuts import render, redirect
from productsApp.forms import ProductForm
from .models import products


# Create your views here.

def productsApp(request):
    return render(request, 'home.html')


def create(request):
    if request.method == "POST":
        fm = ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/show")
    else:
        fm = ProductForm()

    return render(request, 'create.html', {"form": fm})


def show(request):
    data = products.objects.all()
    return render(request, 'show.html', {"cart": data})



