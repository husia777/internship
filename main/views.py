import requests
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse

from main.forms import AuthUserForm, CreateUserForm, FormCalculator
from django.views.generic import View
from django.shortcuts import redirect
from main.models import Headers, Resources, HeroHeaderContent, StatisticContent
from main.services import get_data, coins_data
from django.http import JsonResponse


def home(request):
    resources = Resources.objects.all()
    headers = Headers.objects.all()
    hero_headers = HeroHeaderContent.objects.all()
    statistic_data = StatisticContent.objects.all()
    api_data = coins_data
    print(api_data, 0000000000000000000000)
    context = {
        'statistic_data': statistic_data,
        'api_data': api_data,
        'home': headers[0],
        'headers': headers[1::],
        'hero_headers': hero_headers,
        'resources': resources,
        'calculator': FormCalculator}

    return render(request, 'html/index.html', context)


# context = {
#         'currency': api_data[coin],
#         'api_data': api_data,
#         'home': headers[0],
#         'headers': headers[1::],
#         # 'form': MailingForm,
#         'calculator': FormCalculator}
#
#     return render(request, 'html/index.html', context)
def calculate_income(request):
    if request.method == 'GET':
        form = FormCalculator(request.GET)
        if form.is_valid():
            coin = form.cleaned_data['currency']
            currencies = get_data()
            current_coin_price = currencies[coin]
            request.session['currency'] = current_coin_price

            return JsonResponse({'currency': current_coin_price})


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


def calculator(request):
    hash_rate = request.GET.get('hash_rate')
    currency = int(request.GET.get('currency')) + 1

    data = requests.get(
        f'https://whattomine.com/coins/{currency}.json?hr={hash_rate}.0&p=0.0&fee=0.0&cost=0.0&cost_currency=USD&hcost=0.0&span_br=&span_d=24').json()
    response = {'profit': data['profit'], 'name_coins': data['tag'], 'count': data['estimated_rewards']}
    return JsonResponse(response)
