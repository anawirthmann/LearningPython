p = float(input())
h = float(input())
imc = p / (h*h)

if (imc<18.5):
    classificacao = "Baixo peso"
elif(imc>=18.5) and (imc<=24.9):
    classificacao = "Peso normal"
elif(imc>24.9) and (imc<=29.9):
    classificacao = "Sobrepeso"
elif(imc>29.9) and (imc<=34.9):
    classificacao = "Obesidade grau I"
elif(imc>34.9) and (imc<=39.9):
    classificacao = "Obesidade grau II"
elif(imc>39.9):
    classificacao = "Obesidade grau III"

print("%.2f"%imc)
print(classificacao)
if (imc>24.9):
    peso_ideal = (24.9*(h*h))
    peso_perder = (p - (peso_ideal))
    print("%.2f"%peso_perder)