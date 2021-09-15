from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def method(request):
    return render(request, 'cadastro_app/index.html',)