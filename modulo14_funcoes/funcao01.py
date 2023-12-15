#operação de média
nota1 = input('Insira nota 1: ')
nota2 = input('Insira nota 2: ')

def calcular_media(nota1, nota2):
    media = (float(nota1) + float(nota2)) / 2
    return print('A média das notas é: {}'.format(media))

calcular_media(10, 5)
