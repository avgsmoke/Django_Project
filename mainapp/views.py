from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.forms import FeedbackForm
from mainapp.models import Products
from tehplan45 import settings


def index(request):
    products = Products.objects.all()[:6]
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            messages = f'От: ({form.email})\n ' \
                       f'Имя: {form.full_name} ({form.tel})\n ' \
                       f'Товар: {form.product} \n ' \
                       f'Адрес: {form.address} \n '
            res = send_mail(settings.EMAIL_TITLE, messages, settings.EMAIL_HOST_USER, ['crimecrew_tehplan@mail.ru'])
            if res:
                form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = FeedbackForm()
    context = {
            'form': form,
            'products': products
    }

    return render(request, 'mainapp/index.html', context)


def catalog(request):
    products = Products.objects.all()
    context = {
        'title': 'каталог',
        'products': products,
    }
    return render(request, 'mainapp/catalog.html', context)


def about1(request):
    context = {
        'title': 'каталог',
    }
    return render(request, 'mainapp/about1.html', context)


def about2(request):
    context = {
        'title': 'каталог',
    }
    return render(request, 'mainapp/about2.html', context)


def about3(request):
    context = {
        'title': 'каталог',
    }
    return render(request, 'mainapp/about3.html', context)


def cart(request):
    if request.user.is_authenticated:
        pass


def get_product(request, id):
    info = get_object_or_404(Products, id=id)
    context = {
        'title': info.name,
        'product': info,
    }
    return render(request, 'mainapp/info.html', context)
