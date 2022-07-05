# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.views.decorators.cache import cache_control
from django.views.decorators.cache import cache_control

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def register(request):
    if request.method == 'POST':
       #get form values
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

       #Check if passwords match
       if password == password2:
           #Check username
           if User.objects.filter(username=username).exists():
               messages.error(request, 'That Username is taken')
               return redirect('register')
           else:
               if User.objects.filter(email=email).exists():
                   messages.error(request, 'That Email is Registered')
                   return redirect('register')
               else:
                   user = User.objects.create_user(username=username, password=password,
                                                   first_name=first_name, last_name=last_name, email=email)
                   #login after register
                   # auth.login(request, user)
                   # messages.success(request, 'You are now logged in')
                   # return redirect('index')
                   user.save()
                   messages.success(request, 'You are successfully registered')
                   return redirect('login')
       else:
           messages.error(request, 'Passwords do not match')
           return redirect('register')

    else:
        return render(request, 'accounts/register.html')

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Login Details')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

# @login_required
# @cache_control(no_cache=True, must_revalidate=True)
# def logout(request):
#     auth.logout(request)
    # return render(request,'accounts/login.html')


