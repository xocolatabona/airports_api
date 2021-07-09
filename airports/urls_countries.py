from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), 
    path('asia', views.getCountriesWithAirportsInAsia, name='countriesairportsasia'),
    path('asia', views.getCountriesWithAirportsInAsia, name='countriesairportsasia'),
    path('asia/<str:asianCountry>', views.nativeNameAsianCountry, name='asiancountrynativename'),
]