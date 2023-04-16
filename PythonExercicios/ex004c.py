#Leia o tipo do que foi digitado e coloque na tela o que é

v1 = input("Digite algo: ")

# Python 2 ou anterior
'''
print('O tipo primitivo é ', type(v1))

print('É um Valor Alfanumérico? ',v1.isalnum())
print('É um Valor Alfabético? ',v1.isalpha())
print('É um Valor Númerico? ',v1.isnumeric())
print('É um Valor em Minúsculo? ',v1.islower())
print('É um Valor em Maiúsculo? ',v1.isupper())
print('Só tem espaços? ', v1.isspace())
print('Está capitalizada? ', v1.istitle())
'''

# TODO Python 3
print('O tipo Primitivo dessa variavel é: {} '.format(type(v1)))

print('É um valor Alfanumérico? {} '.format(v1.isalnum()))
print('É um valor Alfabético? {}'.format(v1.isalpha()))
print('É um valor Númerico? {}'.format(v1.isnumeric()))
print('É um valor todo em minusculo? {}'.format(v1.islower()))
print('É um valor todo em maisuculo? {}'.format(v1.isupper()))
print('É um valor apenas com espaços? {}'.format((v1.isspace())))
print('É um valor que está Capitalizado? {}'.format(v1.istitle()))
