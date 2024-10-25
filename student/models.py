from django.db import models

from trainer.models import Trainer


class Student(models.Model):
    gender_options = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    first_name = models.CharField(max_length=40)  # max_length = 255
    last_name = models.CharField(max_length=40)
    profile = models.ImageField(upload_to='students_profile/', null=True)
    email = models.EmailField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(max_length=500)  # max_length = nelimitat
    gender = models.CharField(choices=gender_options, max_length=6)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# python manage.py makemigrations
# python manage.py migrate

# DE RETINUT! DE FIECARE DATA CAND MODIFICATI ELEMENTE DIN MODEL RULATI COMENZILE DE MAI SUS
# PENTRU  A SINCRONIZA TABELA

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    jsbn = models.CharField(max_length=13)
    price = models.IntegerField()
    def __str__(self):
        return f' {self.title} {self.author} {self.published_date} {self.price}'

