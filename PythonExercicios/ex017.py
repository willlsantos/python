# TODO Faça um programa que leia o comprimento do cateto opsto e do cateto adjacente de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))

h = hypot(co, ca)

print('Se o cateto opsoto é {} e o cateto adjacente é {}\nEntão a hipotenusa é {:.2f}'.format(co, ca, h))
