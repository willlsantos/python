#Leia dois números e tente mostrar a soma entre eles

v1 = input("Digite algo: ")


print(v1.isalnum())

if v1.isalnum():
    print('O que você digitou é {} e é Alfanumérico'.format(v1))
elif v1.isalpha():
    print('O que você digitou é {} e é Alfabético'.format(v1))
elif v1.isnumeric():
    print('O que você digitou é {} e é Numérico'.format(v1))
elif v1.islower():
    print('O que você digitou é {} e está com letras minúsculas'.format(v1))
elif v1.isupper():
    print('O que você digitou é {} e está com letras maiúsculas'.format(v1))
