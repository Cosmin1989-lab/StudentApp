from django.urls import path

from intro import views

urlpatterns = [
    path('f_page/', views.first_page, name='fname'),
    path('s_page/', views.second_page, name='sname'),
    path('l_cars/', views.list_of_cars, name='lcars'),
    path('l_books/', views.list_of_books, name='lbooks'),


]