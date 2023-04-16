# Primeiro exemplo aula
'''
nome = input('Qual é o seu nome? ')

print('Prazer em te conhecer {:=^20}!'.format(nome))
'''
# Segundo exemplo aula
'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))

print('A soma vale {}'.format(n1+n2))
'''
# terceiro exemplo aula
'''
n1= int(input('Digite um valor: '))
n2 = int(input('Digite outro Valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2

print('A Soma é {}, o Produto é {}, e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {}, e a potência {}'.format(di, exp))
'''
# quarto exemplo
'''
n1= int(input('Digite um valor: '))
n2 = int(input('Digite outro Valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2

print('A Soma é {}, o Produto é {}, e a divisão é {:.3f}, '.format(s, m, d), end='')
print('Divisão inteira {}, e a potência {}'.format(di, exp))
'''

# Quinto exemplo

n1= int(input('Digite um valor: '))
n2 = int(input('Digite outro Valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2

print('A Soma é {}, \no Produto é {}, e a \ndivisão é {:.3f}, '.format(s, m, d))
print('Divisão inteira {}, e a potência {}'.format(di, exp))