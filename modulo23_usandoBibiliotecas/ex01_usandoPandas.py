import pandas as pd

df = pd.DataFrame(
     {
         "Name": [
             "Braund, Mr. Owen Harris",
             "Allen, Mr. William Henry",
             "Bonnell, Miss. Elizabeth",
         ],
         "Age": [22, 35, 58],
         "Sex": ["male", "male", "female"],
    }
 ) 

df

"""
Pelo exemplo, podemos deduzir que para criar um DataFrame
utilizaremos o método pd.DataFrame(), passando como parâmetro um
dicionário de listas que contém as informações que estarão dentro dele.
Esse DataFrame pode ser armazenado em uma variável, como no exemplo,
em que é atribuído à variável df.

Analisando o DataFrame resultante, podemos observar que cada chave do
dicionário representa uma coluna da tabela, enquanto os valores
associados a essas chaves, as listas, representam as linhas da tabela.
As listas são ordenadas, e cada valor dentro delas corresponde a uma
célula na tabela. A primeira informação de cada lista compõe a primeira
linha da tabela, a segunda informação compõe a segunda linha e assim por
diante.
"""