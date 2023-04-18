valorInicial, numParcelas  = input().split()
txdesconto = float
valorFinal = float
valorParcela = float
desconto = float

if numParcelas == 1:
    txdesconto = 0.05
    desconto = txdesconto*valorInicial
    valorFinal = valorInicial - desconto
    
if numParcelas == 2:
    txdesconto = 0
    desconto = txdesconto*valorInicial
    valorFinal = valorInicial - desconto

if numParcelas == 3:
    txdesconto = 0.05
    desconto = txdesconto*valorInicial
    valorFinal = valorInicial + desconto

if numParcelas == 4:
    txdesconto = 0.1
    desconto = txdesconto*valorInicial
    valorFinal = valorInicial + desconto

print("%.2f" %valorInicial)
print("%.2f" %numParcelas)
print("%.2f" %txdesconto)
print("%.2f" %valorFinal)
print("%.2f" %valorParcela)



