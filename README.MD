# internship
<h1> Quick Start</h1>
<h3>git clone https://github.com/husia777/internship.git</h3><br>
<h3>docker compose up --build</h3><br>
<h2>Команда для востановления данных из дампа</h2>
<h3> cat postgres_localhost-2023_03_01_17_14_34-dump.sql | docker exec -i internship-postgres-1 psql -U postgres -d postgres </h3><br>
Calculator jsonresponse - {"profit": "$8.74", "name_coins": "BTC", "count":"0.000368"}  <br>
url - http://127.0.0.1:8000/calculate/


https://api.coingecko.com/api/v3/coins/{coin_name}

"price_change_24h": 42.158928,
"price_change_percentage_24h": 0.18762,
"price_change_percentage_7d": -4.36913,
"price_change_percentage_14d": -7.29644,
"price_change_percentage_30d": -4.00401,
"price_change_percentage_60d": 33.56477,
"price_change_percentage_200d": -3.62528,
"price_change_percentage_1y": -42.95292,


login to server -  ssh hussein@garinv.online
password - `HusseinZaq123`
command -  cd /usr/src/hussein/
sudo docker compose -f docker-compose.prod.yml up --build 
gunicorn config.wsgi:application --bind 0.0.0.0:8000