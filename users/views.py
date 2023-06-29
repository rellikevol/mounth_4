from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.clean_password2())
            new_user.save()
            return render(request, 'registration/register_done.html', {'user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': user_form})


class UserCreateView(generic.DetailView):
    model = User

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.clean_password2())
            new_user.save()
            return render(request, 'registration/register_done.html', {'user': new_user})
        else:
            return render(request, 'registration/register.html', {'form': user_form})

    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': user_form})
