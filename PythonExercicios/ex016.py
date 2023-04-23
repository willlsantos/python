# TODO Crie um programa que leia um número Real e mostre na tela a sua porção inteira. Ex: 6.127 part inteira é 6
# Dentro do módulo math tem a função que faz isso
'''
from math import modf

n1 = float(input('Digite um número: '))
por = modf(n1)

print('A Parte inteira do número {} é {}'.format(n1, por))
'''
#Resolução Guanabara

import math

n1 = float(input('Digite um número: '))

print('A Parte inteira do número {} é {}'.format(n1, math.trunc(n1)))