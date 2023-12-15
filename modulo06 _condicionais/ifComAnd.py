metaFuncionário = 10000
metaLoja = 25000
vendasFuncionaario = 55000
vendasloja = 40000

if vendasFuncionaario > metaFuncionário and vendasloja > metaLoja:
    bonus = 0.03 * vendasFuncionaario
    print('Bonus do funcionário doi de {}' .format(bonus))
else:
    print('Funcionário não ganhou bônus')