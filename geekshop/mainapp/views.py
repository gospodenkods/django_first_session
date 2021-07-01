from django.shortcuts import render
import json
from django.conf import settings
import functools
import operator

from mainapp.models import Product


def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str


def getjson(obj):
    with open(f"{obj}.json", "r") as read_file:
        return json.load(read_file)


def products(request):
    title = 'продукты/каталог'
    t = convertTuple(settings.STATICFILES_DIRS) + "\menu_json"
    links_menu = getjson(t.replace("\\", "/"))
    products = Product.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
    }
    return render(request=request, template_name='mainapp/products.html', context=context)

# def products(request):
#     title = 'продукты/каталог'
#     links_menu = [
#         {'href': 'products_all', 'name': 'все'},
#         {'href': 'products_home', 'name': 'дом'},
#         {'href': 'products_office', 'name': 'офис'},
#         {'href': 'products_modern', 'name': 'модерн'},
#         {'href': 'products_classic', 'name': 'классика'},
#     ]
#     context = {
#         'title': title,
#         'links_menu': links_menu,
#     }
#     return render(request=request, template_name='mainapp/products.html', context=context)