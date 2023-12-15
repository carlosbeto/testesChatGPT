def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
    except:
        raise ValueError('Email informado não contem @, digite novamente')
    else:
        servidor = email[posicao_a:]
        if 'email' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'Não determinado'
        

email = input('Qual seu e-mail?')
print(descobrir_servidor(email))
        