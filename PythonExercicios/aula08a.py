#Módulos Exemplo1
'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print ('A Raiz de {} é igual a {}'.format(num, raiz))
'''

'''
#Exemplo 2 - Arredondando pra cima
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print ('A Raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
'''
'''
#Exemplo 3 - Arredondando para baixo
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print ('A Raiz de {} é igual a {}'.format(num, math.floor(raiz)))
'''

'''
#Ou Exibindo 2 casas decimais usando máscaras
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print ('A Raiz de {} é igual a {:.2f}'.format(num, raiz))

'''
#Exemplo importando via From
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)

print ('A Raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))