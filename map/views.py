from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Search
#from .forms import SearchForm
import folium
#import geocoder
#import time

# Create your views here.
#import mygeotab
#import pandas as pd
from datetime import datetime, timedelta

# name JCBMW
# serialNumber G79A21002499

lat = 6.210605
lng = -75.596756


def index(request):


    Search.objects.all().last()


    lat = 6.210605
    lng = -75.596756

    cordenadas = str(lat) + "," + str(lng)
    m = folium.Map(location=[lat, lng], zoom_start=18, control_scale=True)
    folium.Marker([lat, lng],  icon=folium.Icon( icon='car', prefix='fa'),
                  popup=cordenadas).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'index.html', context)

