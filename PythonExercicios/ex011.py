# TODO faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#  e a  quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m²

larg = float(input('Digite a Largura da parede: '))
alt = float(input('Digite a Altura da Parede: '))

a = larg * alt

l = 2

result = a / l

print ('Sua parede tem {}m²\nVocê precisa de {:.2} latas de tintas para pintar essa parede'.format(a, result))