from django.db import models


class Trainer(models.Model):


    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    profile = models.ImageField(upload_to="trainer_profiles/", null=True)
    email = models.EmailField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # python manage.py makemigrations
    # python manage.py migrate

    # DE RETINUT! DE FIECARE DATA CAND MODIFICATI ELEMENTE DIN MODEL RULATI COMENZILE DE MAI SUS
    # PENTRU  A SINCRONIZA TABELA
