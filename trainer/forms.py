from django import forms

from student.models import Student
from trainer.models import Trainer


class TrainerForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = '__all__'


        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a last name'}),
            'course': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an course'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an email'})
        }

class TrainerUpdateForm(forms.ModelForm):

    class Meta:
        model = Trainer
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