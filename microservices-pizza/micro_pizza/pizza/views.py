import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.serializers import serialize


# Create your views here.
# from django.utils.decorators import method_decorator
# from django.views import View
from django.views.decorators.cache import cache_control

from pizza.models import Pizza



@login_required(redirect_field_name=None)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def index(request, pid):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_pizza = Pizza.objects.create(title=data['title'], description=data['description'], creator=request.user)
        new_pizza.save()
        return HttpResponse(
            content={
                'id': new_pizza.id,
                'title': new_pizza.title,
                'description': new_pizza.description,
            }
        )
    elif request.method == 'GET':
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse(
            content={
                'id': pizza.id,
                'title': pizza.title,
                'description': pizza.description,
            }
        )


@login_required(redirect_field_name=None)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def listing(request,pid):
    try:
        pizza = Pizza.objects.get(id=pid)
        data = serialize("json", [pizza], fields=['id', 'title', 'description'])
        return HttpResponse(data, content_type='application/json')
    except Pizza.DoesNotExist:
        raise Http404
    return render(request, '404.html')


@login_required(redirect_field_name=None)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def gettenpizza(request):
    if request.user.is_authenticated:
        pizzas = Pizza.objects.order_by('?')[:10]
        return render(request, 'pizza/ten_pizzas.html', {'pizzas': pizzas})
    else:
        return redirect('/login')