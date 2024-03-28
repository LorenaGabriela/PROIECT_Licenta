from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register_medic/', views.register_medic, name = 'register_medic'),
    path('pacienti/',views.pacienti,name="pacienti"),
    path('login_medic/', views.login_medic, name="login_medic"),
    path('logout_medic/', views.logout_user, name="logout_user"),
    path('adauga_pacienti/', views.adaugapacienti,name = "adauga_pacienti"),
    path('stergepacienti/<id>', views.stergepacienti, name='stergepacienti'),
    path('editeaza_pacient/<id>', views.editeaza_pacient, name="editeaza_pacient"),
    path('upload_mamografie_pacient/<id>', views.upload_mamografie_pacient, name="upload_mamografie_pacient")
]
