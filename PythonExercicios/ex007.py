#Todo Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

##Cuidado como calcular, se ligue na ordem de precedencia

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))

soma = n1 + n2

result = soma / 2

#Primeira forma de Print

#print('\nA média das suas notas é {}'.format((n1+n2)/2))

# Segunda forma de Print
print('\nA média das suas notas é {:.1f}'.format(result))