
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import SignupForm, LoginForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                response = redirect('dashboard')
                response.set_cookie('access_token', str(refresh.access_token))
                return response
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
