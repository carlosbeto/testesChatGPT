'''
Quando usamos essa formatação (:+), sempre será colocado sinal 
na frente dos números, não importando se esses números são positivos ou negativos.
'''

custo = 500
faturamento = 270
lucro = faturamento - custo

print('Faturamento foi {:+} e lucro foi {:+}'.format(faturamento, lucro))

