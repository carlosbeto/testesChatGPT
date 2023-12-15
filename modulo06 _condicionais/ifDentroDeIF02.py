meta = 20000
vendas = 25000

if vendas < meta:
    print('Não ganhou bônus')
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print('Ganhou {} de bônus' .format(bonus))
else:
    bonus = 0.03 * vendas
    print('ganhou {} de bônus' .format(bonus))

    """
    Vamos avaliar o exemplo acima:
Nesse exemplo um bônus é calculado baseado no desempenho das vendas.
1)
Caso a meta não seja atingida, não haverá bônus.
2)
Caso as vendas superem a meta em 2x, o bônus é calculado por: Vendas X 7%
3)
Se a meta for superada mas inferior a 2x, o bônus será calculado por : Vendas X 3%
    """