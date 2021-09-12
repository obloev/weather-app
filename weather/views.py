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

