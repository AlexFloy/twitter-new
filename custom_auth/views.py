from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic.edit import CreateView
from custom_auth.forms import CustomUser, LoginForm


class RegisterView(CreateView):
    form_class = CustomUser
    success_url = reverse_lazy('users')
    template_name = 'custom_auth/registration.html'


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users')
    else:
        form = LoginForm()
    return render(request, 'custom_auth/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
