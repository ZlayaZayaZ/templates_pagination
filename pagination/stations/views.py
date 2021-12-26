from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import csv

CONTENT = []
with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        info = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
        CONTENT.append(info)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    paginator_page = paginator.page(page_number)
    content_page = paginator_page.object_list
    context = {
         'bus_stations': content_page,
         'page': page
    }
    return render(request, 'stations/index.html', context)
