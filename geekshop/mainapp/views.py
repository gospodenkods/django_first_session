from django.shortcuts import render
import json
from django.conf import settings
import functools
import operator


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
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request=request, template_name='mainapp/products.html', context=context)