x = int(input())
horas = float
min = float
seg = float

horas = (x//3600)
min = ((x % 3600)//60)
seg = (x % 60)

print(horas,"h:",min,"m:",seg,"s",sep="")
