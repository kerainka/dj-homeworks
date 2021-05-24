import math
from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    stations = []
    with open('data-398-2018-08-30.csv', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations.append(row)

    current_page = request.GET.get('page', 1)
    current_page = int(current_page)
    items_per_page = 10
    total_pages = math.ceil(len(stations) / items_per_page)
    if current_page < 1 or current_page > total_pages:
        current_page = 1

    page_stations = stations[(current_page - 1) * items_per_page: current_page * items_per_page]

    prev_page, next_page = None, None

    path = reverse(bus_stations)
    if current_page > 1:
        prev_page = f'{path}?{urlencode({"page": current_page - 1})}'
    if current_page * items_per_page < len(stations):
        next_page = f'{path}?{urlencode({"page": current_page + 1})}'

    return render(request, 'index.html', context={
        'bus_stations': page_stations,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })

