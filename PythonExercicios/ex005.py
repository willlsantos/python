# TODO Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um número: '))

ante = n1 - 1
suc = n1 + 1

print('O Antecessor é {}, \no número digitado é o {}, \ne o Sucessor é o {}.'.format(ante, n1, suc))

## Correção Guanabara outra forma. Quanto menos variaveis, menos memória seu programa consome.
'''
n = int(input('Digite um número: '))
print('Analisando o valor {}, sei antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

'''