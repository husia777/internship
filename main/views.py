import requests
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from main.forms import AuthUserForm, CreateUserForm, FormCalculator
from django.views.generic import View
from django.shortcuts import redirect
from main.models import Headers


def home(request):
    headers = Headers.objects.all()
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()

    context = {
        'api_data': api_data,
        'home': headers[0],
        'headers': headers[1::],
        # 'form': MailingForm,
        'calculator': FormCalculator}

    return render(request, 'html/index.html', context)


class LoginUserView(LoginView):
    form_class = AuthUserForm
    template_name = 'html/login.html'

    def get_success_url(self):
        self.success_url = 'http://127.0.0.1:8000/home/'
        return self.success_url


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


def subscribe_to_the_newsletter(request):
    current_user = request.user
    current_user.subscribe_to_the_newsletter = True
    current_user.save()
    return render(request, 'html/index.html')
