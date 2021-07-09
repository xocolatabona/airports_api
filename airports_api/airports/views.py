from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests 
from .utility import *

#The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1G5darnYfuJvfPvaGZR9Y3cItm3wMbCQQ5DpZDkB7GQ0'
SAMPLE_RANGE_NAME = 'Hoja 1!A:L'
API_KEY = "private_key"

# Create your views here.
def index(request):
    return render(request, 'airports/index.html', {'no_data': 'no_data'})

@csrf_exempt
def getAllAirports(request):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports_dict = to_dict_list(values[1:], values[0])
        return JsonResponse(airports_dict, safe=False)

@csrf_exempt
def getAirportsByCountry(request, countryName):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports_dict = to_dict_list(values[1:], values[0])
        airports = list(filter(lambda x: countryName.lower() in x["Country"].lower(), airports_dict))
        return JsonResponse(airports, safe=False)

@csrf_exempt
def getAirportsByName(request, airportName):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports_dict = to_dict_list(values[1:], values[0])
        airports = list(filter(lambda x: airportName.lower() in x["Airport Name"].lower(), airports_dict))
        return JsonResponse(airports, safe=False)

@csrf_exempt
def getAirportByIataCode(request, iataCode):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports_dict = to_dict_list(values[1:], values[0])
        airport = list(filter(lambda x: iataCode.lower() in x["IATA Code"].lower(), airports_dict))
        return JsonResponse(airport, safe=False)

@csrf_exempt
def getAirportByIcaoCode(request, icaoCode):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports_dict = to_dict_list(values[1:], values[0])
        airport = list(filter(lambda x: icaoCode.lower() in x["ICAO Code"].lower(), airports_dict))
        return JsonResponse(airport, safe=False)

@csrf_exempt
def getAirportByContinentState(request, continentState):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports_dict = to_dict_list(values[1:], values[0])
        airport = list(filter(lambda x: continentState.lower() in x["Continent/State"].lower(), airports_dict))
        return JsonResponse(airport, safe=False)

@csrf_exempt
def getAirportByUTCTimeZone(request, utcTimeZone):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports_dict = to_dict_list(values[1:], values[0])
        airport = list(filter(lambda x: utcTimeZone.lower() in x["UTC TimeZone"].lower(), airports_dict))
        return JsonResponse(airport, safe=False)

@csrf_exempt
def getAirportByDST(request, dst):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports_dict = to_dict_list(values[1:], values[0])
        airport = list(filter(lambda x: dst.lower() in x["DST"].lower(), airports_dict))
        return JsonResponse(airport, safe=False)

def getCountriesWithAirportsInAsia(request):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports = to_dict_list(values[1:], values[0])
        airports = list(filter(lambda x: x["Continent/State"] != None and "Asia" in x["Continent/State"], airports))
        asian_countries = {}
        url_country = "https://restcountries.eu/rest/v2/region/asia" 
        countries_request = requests.get(url_country)
        for airport in airports:
            if asian_countries.get(airport["Country"]) is None:
                country = list(filter(lambda x: airport["Country"] in x["name"], countries_request.json()))
                if len(country) > 0:
                    asian_countries[airport["Country"]] = {"Name": airport["Country"], "Native Name": country[0]["nativeName"]}

    return JsonResponse(asian_countries, safe=False)

def nativeNameAsianCountry(request, asianCountry):
    url = "https://sheets.googleapis.com/v4/spreadsheets/" + SAMPLE_SPREADSHEET_ID + "/values/" + SAMPLE_RANGE_NAME + "?key=" + API_KEY
    result = requests.get(url).json()
    values = result['values']
    if not values:
        return Http404('No data found.')
    else:
        airports = to_dict_list(values[1:], values[0])
        airports = list(filter(lambda x: x["Continent/State"] != None and "Asia" in x["Continent/State"] and asianCountry.lower() in x['Country'].lower(), airports))
        if len(airports) > 0:
            url_country = "https://restcountries.eu/rest/v2/name/" + airports[0]['Country'] 
            country_request = requests.get(url_country)
            if country_request.status_code == 200:
                country_json = country_request.json()
                country = {"Name": country_json[0]["name"], "Native Name": country_json[0]["nativeName"]}
                return JsonResponse(country, safe=False)
        return Http404('No data found.')


    