from django.shortcuts import render

from django.contrib.gis import geos
from django.contrib.gis import measure
from django.contrib.gis.db.models.functions import Distance

from manage_shops import forms
from manage_shops import models

def get_shops(longitude, latitude, distance):
    current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
    distance_from_point = {'km': distance}
    shops = models.Shops.objects.filter(location__distance_lte=(current_point, measure.D(**distance_from_point))).annotate(distance=Distance('location', current_point)).order_by('distance')
    return shops

def find_shops(request):
    form = forms.LocationDistanceForm()
    shops = []
    if request.POST:
        form = forms.LocationDistanceForm(request.POST)
        if form.is_valid():
            lat = form.cleaned_data['latitude']
            lon = form.cleaned_data['longitude']
            distance = form.cleaned_data['distance']
            if lat and lon and distance:
                shops = get_shops(longitude=lon, latitude=lat, distance=distance)

    return render(request,
        'location_and_address.html',
        {'form': form, 'shops': shops},
        )
