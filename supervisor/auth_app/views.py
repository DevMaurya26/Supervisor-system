from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from main.form import UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .middelwear import alreadyLogedIn # Custom Middelwear made by me(Dev)
# Create your views here.

@alreadyLogedIn
def register_view(request):
    '''
    when user want to register so we have to store data in database using Built in UserCreationFrom provided by django..! 
    '''
    if request.POST:
        # here we are getting data from user and storing in form
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # checking is the form is valid or not?
            user = form.save()
            login(request, user)  # built in login method

            return redirect('dashboard')
    else: # if form is not valid then return null form..
        initial_data = {'username':'','password1':'','password2':'','email':'','first_name':''}
        form = UserRegisterForm(initial=initial_data)

    return render(request, 'auth/RegisterForm.html', {'form': form})

@alreadyLogedIn
def login_view(request):
    if request.POST:
        # here we gonna use authantication form to authenticate user
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():  # checking is the form is valid or not?
            user = form.get_user() #is valid then get user data
            login(request, user)  # built in login method

            return redirect('dashboard')
    else: # if form is not valid then return null form..
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial=initial_data)

    return render(request, 'auth/LoginForm.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):
    # print(request.user.username)
    return render(request,'auth/Dashboard.html')

