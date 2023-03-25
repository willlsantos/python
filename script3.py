#Leia dois números e tente mostrar a soma entre eles

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

num1 = int(num1)
num2 = int(num2)

try:
    result = num1 + num2
    print("O resultado da soma é: ", result)
except:
    print("Um dos valores não é um número inteiro.")
    print("num1 é do tipo: ", type(num1))
    print("num1 é do tipo: ", type(num2))
    print("num1 é do tipo: ", type(result))

# if type(num1) or type(num2) != isinstance(num1, int):
#     print("num1 é do tipo: ", type(num1))
#     print("num2 é do tipo: ", type(num2))
#     print("Um dos valores não é um número. Por favor, digite apenas números.")
    
# else:
#     resultado = num1+num2
#     print("O valor da soma é: ", resultado)