import requests


def get_data():
    api_data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    return api_data


coins_data = get_data()
data = requests.get(f'https://api.coingecko.com/api/v3/coins/bitcoin').json()
response = {'24h': data['price_change_percentage_24h'], '7d': data['price_change_percentage_7d'],
            '30d': data['price_change_percentage_30d'], '1y': data['price_change_percentage_1y']}
print(response)
