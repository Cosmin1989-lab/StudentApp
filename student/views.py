import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.filters import StudentFilters
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student
from trainer.models import Trainer


# CreateView -> clasa de view dezvoltata de Django folosita pentru a genera
# un formular si de a salva datele din formulat in tabela respectiva(in tabela student)

class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'student/create_student.html'  # folosit pentru a specifica calea catre pagina html UNDE va fi generat formularul
    model = Student  # Modelul asociat formularului
    form_class = StudentForm
    success_url = reverse_lazy('home_page')  # folosit pentru a-l redirectiona pe utilizator pe o pagina dupa salvarea datelor din formular



# Metoda get_context_data suplimnenteaza cu date/informatii suplimentae care sunt trimise
    # care template-ul asociat clasei.


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # returneaza un dictionar cu datele pe care trimiteti in html

        context['students'] = Student.objects.all()
        context['trainers'] = Trainer.objects.all()
        context['current_datetime'] = datetime.datetime.now()

        return context

# ListView -> clasa de view dezvoltata de Django folosita pentru a afisa o lista de obiecte asociata modelului



class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'  # Student.objects.all()



    # Metoda care este folosita in view-uri generice pentru a defini ce obiecte sunt trimise si afisate in interfata
    def get_queryset(self):
        return Student.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # in variabila myfilters implmentam functionalitate de filtrare in care pe baza querysetului cautam studentii in functie
        # de ce date se introc in formular
        myfilters = StudentFilters(self.request.GET, queryset=Student.objects.filter(active=True))
        context['all_students'] = myfilters.qs  # salvez studentii care vin in urma filtrarii
        context['filters_form'] = myfilters.form  # trimit in interfata formularul de filtrare

        return context


# UpdateView -> este un view generic dezvoltat de Django si folosit pentru actualizarea
# unui obiect.

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class= StudentUpdateForm
    success_url = '/list_students/'

# DeleteView -> este un view generic dezvoltat de Django si folosit pentru stergerea unui obiect

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-students')

# DetailView -> este un view generic dezvoltat de Django si folosit pentru afisarea detaliilor unui obiect

class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = "student/view_student.html"
    model = Student