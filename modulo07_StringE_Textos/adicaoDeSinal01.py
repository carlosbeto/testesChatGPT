'''
Quando usamos essa formatação (:,), os números passam a ter separadores de milhar.
'''

custo = 5000
faturamento = 2700
lucro = faturamento - custo

print('Faturamento foi {:,} e lucro foi {:,}'.format(faturamento, lucro))
print('')

#print('Faturamento foi {:,} e lucro foi {:,}'.format(faturamento, lucro))
print('Faturamento foi {:+,} e lucro foi {:+,}'.format(faturamento, lucro))

