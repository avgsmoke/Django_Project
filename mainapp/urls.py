
from django.urls import path, include

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('about1/', mainapp.about1, name='about1'),
    path('about2/', mainapp.about2, name='about2'),
    path('about3/', mainapp.about3, name='about3'),
    path('info/<int:id>/', mainapp.get_product, name='info'),
]
