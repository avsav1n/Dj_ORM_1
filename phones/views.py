from django.shortcuts import redirect, render

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    if (key := request.GET.get('sort')):
        sort_keys = {
            'name': {'key': lambda x: x.name},
            'max_price': {'key': lambda x: x.price, 'reverse': True},
            'min_price': {'key': lambda x: x.price}
        }
        phones = sorted(phones, **sort_keys[key])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)


