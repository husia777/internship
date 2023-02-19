from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import View

from main.forms import AuthUserForm, CreateUserForm


class HomePageView(View):
    def get(self, request):
        return render(request, 'html/index.html')


class LoginUserView(LoginView):
    form_class = AuthUserForm
    template_name = 'html/login.html'
    success_url = 'home'


class RegisterUserView(View):
    template_name = 'html/register.html'

    def get(self, request):
        context = {
            'form': CreateUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            username = form.cleaned_data["username"]
            aut_user = authenticate(email=email, password=password, username=username)
            return redirect('login')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
