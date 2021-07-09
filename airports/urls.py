from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('all', views.getAllAirports, name="allairports"),
    path('country/<str:countryName>', views.getAirportsByCountry, name='airportsbycountry'),
    path('name/<str:airportName>', views.getAirportsByName, name='airportsbyname'),
    path('iata/<str:iataCode>', views.getAirportByIataCode, name='airportbyiata'),
    path('icao/<str:icaoCode>', views.getAirportByIcaoCode, name='aiportbyicao'),
    path('continentState/<str:continentState>', views.getAirportByContinentState, name='airportsbycontinentstate'),
    path('utc/<str:utcTimeZone>', views.getAirportByUTCTimeZone, name='airportsbyutc'),
    path('dst/<str:dst>', views.getAirportByDST, name='airportsbydst'),
]