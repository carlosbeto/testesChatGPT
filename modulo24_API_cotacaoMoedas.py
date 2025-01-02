
import requests # type: ignore
import json
import matplotlib.pyplot as plt

cotacao_dolar30d = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30?[start_date=20240101][end_date=20241130]')
cotacoes_dolar_dic = cotacao_dolar30d.json()
lista_cotacoes_dolar = [float(item['bid']) for item in cotacoes_dolar_dic]
print(lista_cotacoes_dolar)
print(len(lista_cotacoes_dolar))

plt.figure(figsize=(10, 5))
plt.plot(lista_cotacoes_dolar)
plt.show()

