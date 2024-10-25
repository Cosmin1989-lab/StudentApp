import django_filters
from django import forms

from trainer.models import Trainer
from student.models import Student


#lookup_expr:

# exact        -> trebuie ca stringul inserat in inputul de cautare sa fie identic cu valoarea salvata in baza dedate
# icontains    -> trebuie ca stringul inserat in inputul de cautare sa fie regasit in alt string salvat in baza de
# date de pe respectiva coloana
# startswith   -> trebuie ca stringul inserat in inputul de cautare sa inceapa cu literele respectiva
# endswith     -> trebuie ca stirngul insearat in inputulul de cautare sa se termine cu literele respectiva

# lte    -> less than or equal to
# lt     -> less than

# gte    -> greater than or equal to
# gt     -> greater than


class TrainerFilters(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a first name'}))
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a last name'}))
    # course = django_filters.CharFilter(lookup_expr='icontains', label='Course', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a course'}))
    email = django_filters.CharFilter(lookup_expr='endswith', label='Email address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an email'}))

    list_courses = list(set([(trainer.course, trainer.course) for trainer in Trainer.objects.all()]))

    course = django_filters.ChoiceFilter(choices=list_courses, widget=forms.Select(attrs={'class': 'form-select'}))



    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'email']