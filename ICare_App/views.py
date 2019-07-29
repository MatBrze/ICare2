from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from ICare_App.forms import UserRegisterForm


class MainView(View):

    def get(self, request):
        return render(request, 'index.html')


class RegisterView(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_email = form.cleaned_data.get('email')
            messages.success(request, f'Konto dla {user_email} zostało utworzone! Zaloguj się')
            return redirect('login')

        return render(request, 'register.html', {'form': form})


class DonateView(View):

    def get(self, request):
        logged_user = request.user.username
        ctx = {
            'user': logged_user
        }
        return render(request, 'form.html', ctx)
