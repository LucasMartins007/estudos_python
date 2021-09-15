from django.shortcuts import render

# Create your views here.
def setimo_periodo(request):
    return render(request, 'setimo_periodo/setimo_periodo.html')