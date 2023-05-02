# Todo Faça um programa que leia o nome dos quatros alunos e mostre na ordem sorteada.
import random

nomes = []

n1 = input('Digite um nome de aluno: ')
n2 = input('Digite um nome de aluno: ')
n3 = input('Digite um nome de aluno: ')
n4 = input('Digite um nome de aluno: ')

nomes = [n1, n2, n3, n4]

#random.shuffle(nomes)
#random.shuffle

print('A ordem dos nomes sorteada é: {}'.format(random.sample(nomes, 4)))