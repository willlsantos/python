#TODO Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = int(input('Digite um valor em metros: '))

cm = m * 100
mm = cm * 10

print('O valor em centimetros é {},\nO valor em milimetros é {}'.format(cm, mm))