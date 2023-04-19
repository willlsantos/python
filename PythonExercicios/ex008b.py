#TODO Escreva um programa que leia um valor em metros e o exiba convertido em KM, Hectometros, decametros
#decimetros, centimetros e milimetros

m = int(input('Digite um valor em metros: '))
km = m / 1000
hm = m /100
deca = m / 10
dc = m * 10
cm = m * 100
mm = cm * 10

print('O valor digitado em: \nKilometros é {} km\nHectometros é {} hm\n Decametros é {} dam\nDecimetros é {} dm\nCentimetros é {} cm\nMilimetros é {} mm'.format(km, hm, deca, dc, cm, mm))