#TODO faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

prod = float(input('Qual é o preço do produto? R$ '))
desc = 0.05

novo_valor = prod - (prod * desc)

print('O novo valor do produto é R${:.2f} '.format(novo_valor))