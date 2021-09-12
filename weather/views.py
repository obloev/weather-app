from django.shortcuts import render
from weather.utils import get_forecast


def current(request):
    city = request.GET.get('city', 'Ghijduwon')
    response = get_forecast(city, 'current')
    if response == None:
        response = [None]
    return render(request, 'current.html', {
        'current': response[0],
    })


def hourly(request):
    city = request.GET.get('city', 'Ghijduwon')
    response = get_forecast(city, 'hourly')
    response_current = None
    if response != None:
        response_current = get_forecast(city, 'current')[0]
    return render(request, 'hourly.html', {
        'current': response_current,
        'hourly': response,
    })


def daily(request):
    city = request.GET.get('city', 'Ghijduwon')
    response = get_forecast(city, 'daily')
    response_current = None
    if response != None:
        response_current = get_forecast(city, 'current')[0]
    return render(request, 'daily.html', {
        'current': response_current,
        'daily': response,
    })

