from django.urls import path
from . import views

urlpatterns = [
    path('', views.setimo_periodo),
]
