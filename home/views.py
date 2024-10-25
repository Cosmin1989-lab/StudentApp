from django.shortcuts import render
from django.views.generic import TemplateView


# TemplateView -> clasa de view definita de Django folosita cu scopul
# de a randa/afisa o pagina html

class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html' # calea catre pagina html pe care doriti da o randati