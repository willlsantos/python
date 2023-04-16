# Leia dois números e tente mostrar a soma entre eles

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

result = num1 + num2

# Uma forma de print mais antiga do Python
# print('O resultado entre a soma de ', num1 ,' e ', num2 , 'é de: ', result )

# Print de uma forma mais simples e mais nova do Python3
print('O resultado entre {} e {} é de: {}'.format(num1, num2, result))
