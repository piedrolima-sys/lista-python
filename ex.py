# Inicializando as variáveis para contar pares e ímpares
pares = 0
impares = 0

# Solicitando que o usuário insira 10 números
for i in range(10):
    numero = int(input(f"Insira o {i+1}º número: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibindo o resultado
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
