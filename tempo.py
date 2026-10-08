segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60
segundos = resto % 60

print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")