#Leia dois números e tente mostrar a soma entre eles

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")



if type(num1) != int:
    print("Um dos valores não é um número. Por favor, digite apenas números.")
    
else:
    resultado = num1+num2
    print("O valor da soma é: ", resultado)