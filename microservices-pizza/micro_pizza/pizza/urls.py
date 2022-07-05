from django.urls import include, path
from .views import listing
from . import views

urlpatterns = [
    path('<int:pid>', listing, name='pizza'),
    path('index', views.gettenpizza, name='index'),
]