from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import CreateView

from .filters import TrainerFilters
from .forms import TrainerForm, TrainerUpdateForm
from .models import Trainer



class TrainerCreateView(LoginRequiredMixin, CreateView):
    model = Trainer
    template_name = 'trainer/create_trainer.html'
    form_class = TrainerForm
    success_url = reverse_lazy('home_page')


class TrainerListView(LoginRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'


    # Metoda care este folosita in view-uri generice pentru a defini ce obiecte sunt trimise si afisate in interfata
    def get_queryset(self):
        return Trainer.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # in variabila myfilters implmentam functionalitate de filtrare in care pe baza querysetului cautam studentii in functie
        # de ce date se introc in formular
        myfilters = TrainerFilters(self.request.GET, queryset=Trainer.objects.filter(active=True))
        context['all_trainers'] = myfilters.qs  # salvez studentii care vin in urma filtrarii
        context['filters_form'] = myfilters.form  # trimit in interfata formularul de filtrare

        return context


# UpdateView -> este un view generic dezvoltat de Django si folosit pentru actualizarea
# unui obiect.


class TrainerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class= TrainerUpdateForm
    success_url = '/list_of_trainers/'

class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')

# DetailView -> este un view generic dezvoltat de Django si folosit pentru afisarea detaliilor unui obiect

class TrainerDetailsView(LoginRequiredMixin, DetailView):
    template_name = "trainer/view_trainer.html"
    model = Trainer
