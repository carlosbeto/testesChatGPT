vendas_meses = [1500, 1727, 1350, 999, 1050, 1027,1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

#plotar o gráfico da forma mais simples
import matplotlib.pyplot as plt

plt.plot(meses, vendas_meses, color='red')
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)+500])
plt.show()