
def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    qtde_cedulas = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(cedulas)):
        qtde_cedulas[i] = valor // cedulas[i]
        valor = valor % cedulas[i]
    return qtde_cedulas

valor_saque = int(input("Digite o valor do saque: "))
qtde_cedulas = calcular_cedulas(valor_saque)

print(f"Quantidade de cédulas: \nR$100: {qtde_cedulas[0]} \nR$50: {qtde_cedulas[1]} \nR$20: {qtde_cedulas[2]} \nR$10: {qtde_cedulas[3]} \nR$5: {qtde_cedulas[4]} \nR$2: {qtde_cedulas[5]} \nR$1: {qtde_cedulas[6]}")
