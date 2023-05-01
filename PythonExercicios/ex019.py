# TODO Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
# Ordem lista

import random

n1 = input('Digite o primeiro aluno: ')
n2 = input('Digite o segundo aluno: ')
n3 = input('Digite o terceiro aluno: ')
n4 = input('Digite o quarto aluno: ')

List = [n1, n2, n3, n4]

escolhido = random.choice(List)

print('O Aluno escolhido foi: {}'.format(escolhido))