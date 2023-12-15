"""
Nessa parte, vamos te explicar algumas comparações que em um primeiro momento 
não são tão simples de compreender.

Veja o exemplo ao abaixo:

O Usuário não forneceu nenhum valor para as duas perguntas feitas pelo 
Python através da função INPUT().
Ao invés de retornar algo como vazio ou simplesmente nada, o retorno 
foi de um erro no código. O que torna mais estranho é que o erro está 
representado na linha 4 onde é feito um cálculo simples de subtração entre 
as variáveis faturamento e custo.

"""
faturamento = input('Qual foi o faturamento da loja nesse mês?')
custo = input('Qual foi o custo da loja nesse mês?')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print('O lucro da loja foi de: ' . format(lucro))
else:
    print('O faturamento e o custo devem ser informados')    




