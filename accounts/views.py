from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from recipes.models import Recipe
from.forms import RegistrationForm

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})

    else:
        return render(request, 'accounts/register.html')




def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'INVALID CREDENTIALS, TRY AGAIN')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')


@login_required
def favorite_add(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe in request.user.profile.favorites.all():
        recipe.favorites.remove(request.user.profile)
    else:
        recipe.favorites.add(request.user.profile)
    return redirect('favorite_list')


@login_required
def favorite_list(request):

    return render(request, 'accounts/favorites.html',)

