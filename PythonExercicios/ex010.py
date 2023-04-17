#TODO Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# considere U$ 1,00 = 3,27

din = int(input('Quanto de dinheiro você tem na carteira?: '))

preco_dol = 3.27
compra_dol = din / preco_dol

print('Com R${}, você pode comprar U${:.2f} Dólares'.format(din, compra_dol))