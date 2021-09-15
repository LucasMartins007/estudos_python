from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def method(request):
    return render(request, 'minha_conta_app/index.html',)