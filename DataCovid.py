import json
from urllib import request
from tabulate import tabulate

url = "https://data.covid19.go.id/public/api/prov.json"

response = request.urlopen(url)

data = json.loads(response.read())

for covid in data['list_data']:
    print(f'- {covid["key"]}: ')
    print(f' Positif: {covid["jumlah_kasus"]}')
    print(f' Sembuh: {covid["jumlah_sembuh"]}')
    print(f' Meninggal: {covid["jumlah_meninggal"]}')


