vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeteira', ['microondas'], 'iphone']

lista_aux = list(zip(vendas_produtos, produtos))
lista_aux.sort(reverse = True)
produtos = [produto for vendas, produto in lista_aux]
print(produtos)

"""
Aqui, temos 2 listas separadas mas que se
relacionam entre si.
Sabemos que se por exemplo ordernarmos a lista de
vendas_produtos do maior para o menor nada
acontecerá na nossa lista produtos.
Ou seja, as posições que antes estavam “casadas”
agora estão distintas.
Antes de qualquer tratamento, precisamos UNIR
essas duas listas. Uma boa forma é transformar
essas duas listas em uma única lista de tuplas.
Para isso, usaremos a função ZIP() que já vimos
anteriormente no módulo de dicionários.
Possuindo a lista de tuplas é só aplicarmos o
unpacking usando o List Comprehension como
apresentado na figura ao lado.

"""