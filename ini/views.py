from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def indexkg(request):
    return render(request, "indexkg.html")

def indexen(request):
    return render(request, 'indexen.html')

def galery(request):
    return render(request, "galery.html")

def galerykg(request):
    return render(request, "galerykg.html")

def galeryen(request):
    return render(request, "galeryen.html")
