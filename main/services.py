import requests


def get_data():
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    return api_data


coins_data = get_data()
