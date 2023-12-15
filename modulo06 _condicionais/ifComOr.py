metaFuncionário = 10000
metaLoja = 25000
vendasFuncionaario = 15000
vendasloja = 0

if vendasFuncionaario > metaFuncionário or vendasloja > metaLoja:
    bonus = 0.03 * vendasFuncionaario
    print('Bonus do funcionário doi de {}' .format(bonus))
else:
    print('Funcionário não ganhou bônus')