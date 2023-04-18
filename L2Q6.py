m, d = input().split()
m = int(m)
d = int(d)
dias = int
colunas = int
ultima_coluna = int
dias_1coluna = int

#conferindo numero de dias do mes
if (m == 2):
    dias = 28
elif (m == 1):
    dias = 31    
elif (m>2) and (m<=7) and ((m%2) == 0):
    dias = 30
elif (m>2) and (m<=7) and ((m%2) != 0):
    dias = 31
elif (m>7) and ((m%2) == 0):
    dias = 31
elif (m>7) and ((m%2) != 0):
    dias = 30

#conferindo primeira coluna e anulando ela
dias_1coluna = (7 - (d-1))
dias = dias - dias_1coluna

#Conferindo se tem ultima coluna
if ((dias%7) == 0):
    ultima_coluna = 0
else:
    ultima_coluna = 1

#somando numero de colunas e voltando com a primeira
colunas = 1 + (dias//7) + ultima_coluna

print(colunas)
