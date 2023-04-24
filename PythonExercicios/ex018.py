#TODO faça um programa que leia um angulo qualquer e mostre na
# tela o valor de seno, coseno e tangente desse angulo.
from math import cos, sin, tan, radians
ang = float(input('Digite um ângulo: '))

sen = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))

print('O ângulo é {}º, o Seno é {:.2f},\nCosseno é {:.2f} e a Tangente é {:.2f}'.format(ang, sen, cose, tang))