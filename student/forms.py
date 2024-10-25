from django import forms

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter a description'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': forms.Select(attrs={'class': 'form-select'})
        }

    # Aceasta metoda este folosita pentru a verifica corectitudinea datelor introduse
    # in formaular in caz contrar se genereaza o eroare

    def clean(self):
        cleaned_data = self.cleaned_data

        # Unicitate pe adresa de email
        get_email = cleaned_data.get('email')
        check_email = Student.objects.filter(email=get_email)
        if check_email:
            msg = 'Email already exists!'
            self.add_error('email', msg)  # adaugam pe campul email mesajul de eroare

        # O validare pentru unicitate pe first_name SI last_name. Nu trebuie sa existe 2 studenti cu acelasi first_name si last_name
        get_first_name = cleaned_data.get('first_name')
        get_last_name = cleaned_data.get('last_name')
        check_name = Student.objects.filter(first_name=get_first_name, last_name=get_last_name)
        if check_name:
            msg = 'First name and last name already exists!'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        # O validare in care sa nu salvez inregistrare daca START_DATE > END_DATE
        get_start_date = cleaned_data.get('start_date')
        get_end_date = cleaned_data.get('end_date')
        if get_start_date >= get_end_date:
            msg = 'Start date is greater than or equal to end date '
            self.add_error('start_date', msg)

        # O validare in care utilizatorul este obligat sa introduca minim 10 caractere in campul description

        get_description = cleaned_data.get('description')
        if len(get_description) < 10:
            msg = 'Description must be at least 10 characters long!'
            self.add_error('description', msg)

        return cleaned_data

class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter a first name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter a last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an email'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter a description'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': forms.Select(attrs={'class': 'form-select'})
        }