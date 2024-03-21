from django.db import models
from django.contrib.auth.models import User


class Medici(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nume_medic = models.CharField(max_length=100)
    prenume_medic = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email_medic = models.EmailField(max_length=100)
    telefon_medic = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.nume_medic + ' ' + self.prenume_medic


class Pacienti(models.Model):
    nume_pacient = models.CharField(max_length=100)
    prenume_pacient = models.CharField(max_length=100)
    email_pacient = models.EmailField(max_length=100)
    telefon_pacient = models.CharField(max_length=12)
    data_nastere = models.DateField()
    sex_pacient = models.CharField(max_length=50)

    def __str__(self):
        return self.nume_pacient + ' ' + self.prenume_pacient
