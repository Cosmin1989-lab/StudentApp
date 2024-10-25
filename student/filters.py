import django_filters
from django import forms

from student.models import Student
from trainer.models import Trainer


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


class StudentFilters(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a first name'}))
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a last name'}))
    # email = django_filters.CharFilter(lookup_expr='endswith', label='Email address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an email'}))

    list_emails = list(set([(student.email, student.email) for student in Student.objects.all()]))

    email = django_filters.ChoiceFilter(choices=list_emails, widget=forms.Select(attrs={'class': 'form-select'}))


    # start_date = django_filters.DateFilter(label="Start date", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    start_date_gte = django_filters.DateFilter(field_name='start_date', lookup_expr='gte', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date_lte = django_filters.DateFilter(field_name='start_date', lookup_expr='lte', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    list_trainers = [(trainer.id , trainer) for trainer in Trainer.objects.all()]

    # trainer = django_filters.ChoiceFilter(choices=list_trainers, widget=forms.Select(attrs={'class': 'form-select'}))
    trainer = django_filters.ChoiceFilter(choices=list_trainers, widget=forms.RadioSelect())


    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'start_date_gte', 'start_date_lte', 'trainer']