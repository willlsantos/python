# TODO Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = float(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos KMs você rodou? '))

cd = 60
ckm = 0.15

result = (d * cd) + (km * ckm)

print('Você ficou {} dias com o carro e rodou {} KMs\n O valor do aluguém é de {:.2f}'.format(d, km, result))
