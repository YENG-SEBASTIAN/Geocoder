from django.shortcuts import render
from django.http import HttpResponse

import folium
import geocoder
# Create your views here.


def index(request):
    location = geocoder.osm("SH Building")
    lat = location.lat
    lng = location.lng
    country = location.county
    map = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([lat, lng], tooltip='Click for more', 
                  popup=country).add_to(map)
    html_form = map._repr_html_()
    context = {
        "map":html_form,
    }
    return render(request, "index.html", context)