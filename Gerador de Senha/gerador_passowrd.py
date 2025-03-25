from random import choices
from string import ascii_letters, digits, punctuation

print('=' * 20)
print('GERADOR DE SENHAS')
print('=' * 20)

# Vai definir os carecteres para a password
caracteres = ascii_letters + digits + punctuation

# Solicita as informações como quantidade de senhas e letras por senha
quant_senhas = int(input('Quantidade de senhas: '))
quant_caracteres = int(input('Quantidade de caracteres por senha: '))

print('\nSuas senhas geradas:')
print('=' * 20)

# Gera e exibe as senhas
for _ in range(quant_senhas):
    senha = ''.join(choices(caracteres, k=quant_caracteres))
    print(senha)

print('=' * 20)
print('\U000026A0 Guarde sua senha com segurança!')