preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho'], ['cafeteira', ['microondas'], ['iphone']]

#usando método tradiciona
impostos = []
for item in preco_produtos:
    impostos.append(item * 0.3)
print(impostos) 

#usando ListCpmprehension
print('')
impostos = [preco * 0.3 for preco in preco_produtos]
print(impostos)

"""
Essencialmente o que ocorre aquié:

Na primeira solução (“Tradicional”):
Criamos uma variável item que percorre a listapreço_produtos, que 
explicitamente adiciona '(.append)' o valor calcula do nalistaimpostos.

Nasegundasolução:
O método .append não é explícito. A leitura da linha de código seria:
“para cada preço da lista preco_produtos será calculado um item da listaimposto. Esse valor
será calculado por preço*0.3”
"""