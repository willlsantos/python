#Leia o tipo do que foi digitado e coloque na tela o que é

v1 = input("Digite algo: ")

# Python 2 ou anterior
print('O tipo primitivo é ', type(v1))

print('É um Valor Alfanumérico? ',v1.isalnum())
print('É um Valor Alfabético? ',v1.isalpha())
print('É um Valor Númerico? ',v1.isnumeric())
print('É um Valor em Minúsculo? ',v1.islower())
print('É um Valor em Maiúsculo? ',v1.isupper())
print('Só tem espaços? ', v1.isspace())
print('Está capitalizada? ', v1.istitle())
#print('É um Valor que possui alguma Valor em Maiúsculo?',v1.is())

# TODO Python 3
