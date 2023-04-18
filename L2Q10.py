tt1, vt1, tt2, vt2 = (input()).split()
tt1 = int(tt1)
tt2 = int(tt2)
vt1 = int(vt1)
vt2 = int(vt2)

#transformando em horas e min
t1_min = tt1 // 60
t2_min = tt2 // 60
t1_h = t1_min / 60
t2_h = t2_min / 60

#calculando penalizacoes
if(tt1==0) or (tt2==0):
    pena0 = 1000
else:
    pena0 = 0

if (t1_min<=29):
    pena1 = (30-t1_min)*2
elif (t1_min>=31):
    pena1 = (30-t1_min)

if (t2_min<=29):
    pena2 = (30-t2_min)*2
elif (t2_min>=31):
    pena2 = (30-t2_min)

vmedia1 = 30 /t1_h 
vmedia2 = 30 /t2_h

print(t1_min)
print(t1_h)
print(t2_min)
print(t2_h)
print(vmedia1)
print(vmedia2)
print(pena0)
print(pena1)
print(pena2)