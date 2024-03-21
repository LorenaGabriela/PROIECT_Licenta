from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth, AbstractUser
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .models import Medici
from .forms import MedicRegistrationForm

def home(request):
    return render(request, 'medical/home.html')


def pacienti(request):
    return render(request, 'medical/pacienti.html')


@csrf_protect
def register_medic(request):
    form = MedicRegistrationForm()

    if request.method == 'POST':
        form = MedicRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacienti')
    context = {'registerform': form}
    return render(request, 'medical/register_medic.html',context=context)


def login_medic(request):
    if request.user.is_staff:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username.strip() and password.strip():
                user = authenticate(request,username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('pacienti.html')
                else:
                    messages.info(request, 'Invalid Username or Password')
                    return redirect('login_medic.html')
            else:
                messages.error(request, 'Vă rugăm să completați toate câmpurile.')
        return render(request, 'medical/login_medic.html')


def logout_user(request):
    logout(request)
    return render(request,'login_medic.html')


# def pacienti(request):
#     medic_autentificat = Medici.objects.get(username=request.user.username)
#     return render(request, 'medical/pacienti.html')