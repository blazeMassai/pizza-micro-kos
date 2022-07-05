from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.cache import cache_control

@login_required(redirect_field_name=None)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def home(request):
    if request.user.is_authenticated:
        return render(request, 'pages/home.html')
    else:
        return redirect('/login')





@login_required(redirect_field_name=None)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def about(request):
    if request.user.is_authenticated:
        return render(request, 'pages/about.html')
    else:
        return redirect('/login')
