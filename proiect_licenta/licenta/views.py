from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth, AbstractUser
from django.contrib import messages


def home(request):
    return render(request, 'medical/home.html')


def pacienti(request):
    return render(request, 'medical/pacienti.html')


def register_medic(request):
    if request.method == 'POST':
        username = request.POST['username']
        nume_medic = request.POST['nume_medic']
        prenume_medic = request.POST['prenume_medic']
        email = request.POST['email_medic']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Contul exista deja!')
                return redirect(register_medic)
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=nume_medic,last_name=prenume_medic)
                user.set_password(password)
                user.save()
                return redirect('home')
    else:
        return render(request, 'medical/register_medic.html')

