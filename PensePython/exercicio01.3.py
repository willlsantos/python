# Distância total em quilômetros
distancia_km = 10

# Tempo total em minutos e segundos
tempo_total_minutos = 42
tempo_total_segundos = 42

# Converter tempo total para minutos
tempo_total = tempo_total_minutos + tempo_total_segundos / 60

# Converter distância total para milhas (1 km = 0.621371 mi)
distancia_mi = distancia_km * 0.621371

# Calcular passo médio em minutos por milha
passo_medio_min_milha = tempo_total / distancia_mi

# Calcular velocidade média em milhas por hora
velocidade_media_mi_h = distancia_mi / (tempo_total / 60)

# Converter passo médio para minutos e segundos
passo_medio_min, passo_medio_seg = divmod(int(passo_medio_min_milha * 60), 60)

# Imprimir resultados
print(f"Passo médio: {passo_medio_min} minutos e {passo_medio_seg} segundos por milha")
print(f"Velocidade média: {velocidade_media_mi_h:.2f} milhas por hora")