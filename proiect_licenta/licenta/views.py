from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth, AbstractUser
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from .models import Pacienti

from .forms import MedicRegistrationForm,LoginForm,PacientiForm


def home(request):
    return render(request, 'medical/home.html')


@csrf_protect
def register_medic(request):
    form = MedicRegistrationForm()

    if request.method == 'POST':
        form = MedicRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_medic')
    context = {'registerform': form}
    return render(request, 'medical/register_medic.html',context=context)


def login_medic(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            messages.success(request, "You are Logged In")
            if user is not None:
                auth.login(request, user)

                return redirect("pacienti")

    context = {'loginform': form}

    return render(request, 'medical/login_medic.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')


# @login_required(login_url="login_medic")
def pacienti(request):
    pacienti = Pacienti.objects.all()
    form = PacientiForm()
    context = {'pacienti' : pacienti, "form" : form}
    return render(request, 'medical/pacienti.html', context)


def adaugapacienti(request):
    if request.method == 'POST':
        form = PacientiForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = PacientiForm()
            pacienti = Pacienti.objects.all()
            context = {'pacienti': pacienti,'form': form}
            return render(request,'medical/adauga_pacienti.html',context)
    else:
        form = PacientiForm()
        pacienti = Pacienti.objects.all()
        context = {'persoane': pacienti, 'form': form}
        return render(request, 'medical/adauga_pacienti.html',context)


def stergepacienti(request,id):
    pacient = Pacienti.objects.get(pk=id)
    pacient.delete()
    return redirect('pacienti')


def editeaza_pacient(request, id):
    pacient = get_object_or_404(Pacienti, pk=id)
    if request.method == 'POST':
        form = PacientiForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            return redirect('pacienti')
    else:
        form = PacientiForm(instance=pacient)
    return render(request, 'medical/editeaza_pacient.html', {'form': form})

