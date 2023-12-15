produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
produto = input('Insira o nome do produto em letra minúscula: ')
estoque = [100, 150, 100, 120, 70, 180, 80]

if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('temos {} unidades de {} no estoque'.format(qtde_estoque, produto))
else:
    print('{} não existe no estoque. '.format(produto))