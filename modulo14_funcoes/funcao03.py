'''
Nesse caso estamos avaliando quais vendedores bateram a meta.
Podemos perceber que nossa função retorna uma tupla com 2 valores:
• % que bateram a meta(perc_baterammeta);
• Pessoas que bateram a meta (vendedores_acima_media)
'''

meta = 10000
vendas = {
    'João' : 15000,
    'Julia':27000,
    'Marcus':9900,
    'Maria':3750,
    'Ana':10300,
    'Alon':7870,
}

def calculo_meta(meta, venda):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)
    perc_baterammeta = len(bateram_meta)/len(vendas)
    return perc_baterammeta, bateram_meta

p_meta, vendedores_acima_meta = calculo_meta(meta, vendas)
print(p_meta)
print(vendedores_acima_meta)