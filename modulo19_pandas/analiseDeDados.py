import pandas as pd

#encoding='latin1', enconding='ISO-8859-1', 
enconding='utf-8'

vendas_df = pd.read_csv (r'C:\Users\ca049341\Documents\MEUS DOCS\testePython.csv', sep = ';')

print(vendas_df)
#pd.display(vendas_df)