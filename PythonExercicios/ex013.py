# TODO faça um algoritmo que leia o salário de um funcionário, e mostre seu novo salário com 15% de aument

sal_atual = float(input('Digite o seu salário: R$'))

aum = 0.15
novo_sal = str(round(sal_atual + (sal_atual * aum), 2)).replace('.', ',')

print('O seu novo salário é de R${}'.format(novo_sal))
