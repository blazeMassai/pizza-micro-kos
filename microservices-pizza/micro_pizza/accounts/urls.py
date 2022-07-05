from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    # path('logout',views.logout, name='logout'),
    re_path(r'^logout$', LogoutView.as_view(),  name='logout'),
]
