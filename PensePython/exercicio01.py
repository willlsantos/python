# Solicitar ao usuário para inserir minutos e segundos
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# Converter minutos e segundos para segundos totais
total_segundos = (minutos * 60) + segundos

print(f"A quantidade total de segundos é: {total_segundos} segundos.")