from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('register_medic/', views.register_medic, name = 'register_medic'),
    path('pacienti/',views.pacienti,name="pacienti")
]