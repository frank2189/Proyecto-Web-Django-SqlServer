
from django.contrib import admin
from django.urls import path

from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mostrar/', views.mostrarConsulta1, name='mostrarConsulta1'),
    path('mostrar2/', views.mostrarConsulta2, name='mostrarConsulta2'),
]