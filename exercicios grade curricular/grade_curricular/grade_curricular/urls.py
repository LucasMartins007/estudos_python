"""grade_curricular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('primeiro-periodo/', include('primeiro_periodo.urls')),
    path('segundo-periodo/', include('segundo_periodo.urls')),
    path('terceiro-periodo/', include('terceiro_periodo.urls')),
    path('quarto-periodo/', include('quarto_periodo.urls')),
    path('quinto-periodo/', include('quinto_periodo.urls')),
    path('sexto-periodo/', include('sexto_periodo.urls')),
    path('setimo-periodo/', include('setimo_periodo.urls')),
    path('oitavo-periodo/', include('oitavo_periodo.urls'))
]
