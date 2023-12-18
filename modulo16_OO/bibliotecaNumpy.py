"""
Outro método muito comum, principalmente quando estamos tratando dados estatisticamente, é
o numpy. Segue abaixo o link da documentação: https://numpy.org/doc/stable/user/tutorials_index.html
Vamos usar o Numpy juntamente do Matplotlib que vimos anteriormente. 
Para importar o Numpy vamos usar o comando abaixo:
Import numpy as np
Aqui vamos replicar o exemplo anterior, mas utilizando o numpy para gerar números aleatórios
de vendas (linha 1). Já na linha 2 vamos usar o método .arange() para
criação de 50 meses que coreesponderão as vendas geradas aleatoriamente.
"""

import numpy as np
import matplotlib.pyplot as plt

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)
print(meses)
print('')
#plt.plot(meses, vendas) - Na linha abaixo foi inclu[ido o metodo 'Color' mudando a cor das linhas do gráfico]
plt.plot(meses, vendas, color='red')
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()
