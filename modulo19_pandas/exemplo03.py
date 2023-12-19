meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print('Produtos acima da meta.: ', produtos_acima_meta)

"""
Mais um caso onde o list comprehension nos auxilia a reduzir as linhas de código. Este caso é ainda menos intuitivo,
principalmente no início da jornada na programação .
LEMBRANDO, nada disso é obrigatório, são formas distintas de se escrever onde o resultado final é o mesmo.
"""
