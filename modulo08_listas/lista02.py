produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
vendas = [1000, 1500, 350, 270,900]

print('As vendas de {} foram de {}'.format(produtos[1], vendas[1]))
print('')
print('Agora que sabemos como acessar os itens da lista por seus respectivos índices, ')
print('vamos aprender como fazer o inverso. Ou seja, descobrir qual o índice de um item conhecido.')

print('')

i = produtos.index('mouse')
print('O valor de i é: ' + str(i))
print('O produto da posição i é: ' + str(produtos[i]))
