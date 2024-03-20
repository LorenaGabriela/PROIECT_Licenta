from django.db import models


class Medici(models.Model):
    nume_medic = models.CharField(max_length=100)
    prenume_medic = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email_medic = models.EmailField(max_length=100)
    telefon_medic = models.CharField(max_length=12)

    def __str__(self):
        return self.nume_medic + ' ' + self.prenume_medic

