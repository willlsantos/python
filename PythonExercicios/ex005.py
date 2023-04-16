# TODO Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um número: '))

ante = n1 - 1
suc = n1 + 1

print('O Antecessor é {}, \no número digitado é o {}, \ne o Sucessor é o {}.'.format(ante, n1, suc))