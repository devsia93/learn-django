from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import FlightForm
# Create your views here.


def flights(request):
    f = Flight.objects.all()
    context = {
        'flights': f,
    }
    return render(request, 'flight/index.html', context)


def flight(request, id_flight):
    f = get_object_or_404(Flight, pk=id_flight)
    context={
        "flight": f,
    }
    return render(request, 'flight/flight.html', context)


def airports(request):
    if request.method == 'POST':
        f = FlightForm(request.POST)
        if f.is_valid():
            f.save()

    a = Airport.objects.all()
    context = {
        'airports': a,
        'flight_form': FlightForm(),
    }
    return render(request, 'flight/index.html', context)


def date_filter(request):
    if request.method == "GET":
        start_date = request.GET.get('start_date')
        d = None
        if start_date:
            d = Flight.objects.filter(date_pub__gte=start_date)
        return render(request, 'flight/date_filter.html', context={'d':d, 'start_date':start_date})
