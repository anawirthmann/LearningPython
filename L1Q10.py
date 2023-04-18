N = int(input())
cem = int
cinq = int
vinte = int
dez = int
cinco = int
dois = int
um = int
saque = int

print(N)

cem = N // 100
print(cem, "nota(s) de R$ 100,00")

saque = N-(cem*100)
cinq = saque//50
print(cinq, "nota(s) de R$ 50,00")

saque = N-(cem*100)-(cinq*50)
vinte = saque//20
print(vinte, "nota(s) de R$ 20,00")

saque = N-(cem*100)-(cinq*50)-(vinte*20)
dez = saque//10
print(dez, "nota(s) de R$ 10,00")

saque = N-(cem*100)-(cinq*50)-(vinte*20)-(dez*10)
cinco = saque//5
print(cinco, "nota(s) de R$ 5,00")

saque = N-(cem*100)-(cinq*50)-(vinte*20)-(dez*10)-(cinco*5)
dois = saque//2
print (dois, "nota(s) de R$ 2,00")

saque = N-(cem*100)-(cinq*50)-(vinte*20)-(dez*10)-(cinco*5)-(dois*2)
um = saque//1
print(um, "nota(s) de R$ 1,00")