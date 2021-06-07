from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Phone


def index(request):
    return redirect(reverse(show_catalog))


def show_catalog(request):
    sort = request.GET.get('sort')

    if sort:
        phones = Phone.objects.order_by(sort)
    else:
        phones = Phone.objects.all()

    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phones': phone
    }
    return render(request, template, context)


