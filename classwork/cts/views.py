from django.shortcuts import render, redirect, get_object_or_404
from .models import City
from .forms import CityForm

def home(request):
    cities = City.objects.all()
    return render(request, 'home.html', context={'cities': cities})


def record(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'record.html', context={'city': city})


def create(request):
    if request.method == 'POST':
        cityfrom = CityForm(request.POST)
        if cityfrom.is_valid():
            cityfrom.save()
            return redirect('home') 
    return render(request, 'create.html', context={'form': CityForm()})


def update(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        cityfrom = CityForm(request.POST, instance=city)
        if cityfrom.is_valid():
            cityfrom.save()
            return redirect('home') 
    return render(request, 'update.html', context={'form': CityForm(instance=city)})


def delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    return redirect('home')