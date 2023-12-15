# Solicitar ao usuário para inserir a quantidade em quilômetros
quilometros = float(input("Digite a quantidade em quilômetros: "))

# Fator de conversão de quilômetros para milhas
fator_conversao = 0.621371

# Converter quilômetros para milhas
milhas = quilometros * fator_conversao

print(f"A quantidade equivalente em milhas é: {milhas} milhas.")
