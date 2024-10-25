from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    return HttpResponse('Hello world!')


def second_page(request):
    return HttpResponse('Hello world, again!')


def list_of_cars(request):
    context = {
        'all_cars':[
            {
                'name_of_brand': 'Tesla',
                'is_electric': True,
                'year': 2023,
                'color': 'black'
            },
            {
                'name_of_brand': 'Mercedes',
                'is_electric': False,
                'year': 2024,
                'color': 'black'
            },
            {
                'name_of_brand': 'Dacia',
                'is_electric': False,
                'year': 2022,
                'color': 'blue'
            },
        ]
    }

    return render(request, 'intro/list_cars.html', context)


# Pasii pentru implementarea functiei cars:

# STEP1: In fisierul views.py din aplicatia intro, am definit o functie numita list_of_cars
# in care s-a definit in variabila context pe cheia all_cars o lista de dictionare (json)

# STEP2: In folderul templates s-a adaugat un nou folder numit intro in care s-a adaugat
# un fisier .html numit list_cars

# STEP3: In fisierul urls.py din aplicatia intro, s-a definit path() pentru apelarea functiei
# list_of_cars (ex. path('l_cars/', views.list_of_cars, name='lcars') )

# STEP4: In folderul intro din folderul templates, in fisierul .html numit list_cars s-a adaugat
# codul .html pentru definirea tabelui in care datele sunt randate.



def list_of_books(request):
    context = {
        'all_books':[
            {
                'name_of_book': 'Mizerabilii',
                'best_seller': True,
                'year': 2023,
                'category': 'Literatura clasica'
            }

        ]
    }

    return render(request, 'intro/list_books.html', context)