import requests
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse

from main.forms import AuthUserForm, CreateUserForm
from django.views.generic import View
from django.shortcuts import redirect
from main.models import Headers, Resources, HeroHeaderContent, StatisticContent
from main.services import coins_data
from django.http import JsonResponse


def home(request):
    resources = Resources.objects.order_by('id')
    headers = Headers.objects.order_by('id')
    hero_headers = HeroHeaderContent.objects.order_by('id')
    statistic_data = StatisticContent.objects.order_by('id')
    api_data = coins_data
    coin_for_statistic = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    context = {
        'statistic_data': statistic_data,
        'coin_for_statistic': coin_for_statistic,
        'api_data': api_data,
        'home': headers[0],
        'headers': headers[1::],
        'hero_headers': hero_headers,
        'resources': resources,
    }

    return render(request, '../templates/html/index.html', context)


class LoginUserView(LoginView):
    form_class = AuthUserForm
    template_name = '../templates/html/login.html'

    def get_success_url(self):
        self.success_url = reverse('home')
        return self.success_url


class RegisterUserView(View):
    template_name = '../templates/html/register.html'

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
    return render(request, '../templates/html/index.html')


def calculator(request):
    hash_rate = request.GET.get('hash_rate')
    currency = int(request.GET.get('currency')) + 1

    data = requests.get(
        f'https://whattomine.com/coins/{currency}.json?hr={hash_rate}&cost_currency=USD').json()
    response = {'profit': data['profit'], 'name_coins': data['tag'], 'count': data['estimated_rewards']}
    return JsonResponse(response)


def chart(request):
    currency = request.GET.get('currency')
    data = requests.get(f'https://api.coingecko.com/api/v3/coins/{currency}').json()
    response = {'24h': data['market_data']['price_change_percentage_24h'],
                '7d': data['market_data']['price_change_percentage_7d'],
                '30d': data['market_data']['price_change_percentage_30d'],
                '1y': data['market_data']['price_change_percentage_1y']}
    return JsonResponse(response)
