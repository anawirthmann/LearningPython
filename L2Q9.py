hora_i, min_i, hora_f, min_f = (input()).split()
hora_i = int(hora_i)
hora_f = int(hora_f)
min_i = int(min_i)
min_f = int(min_f)

duracao_min = ((hora_f*60) + min_f) - ((hora_i*60) + min_i)

if (duracao_min <= 0):
    duracao_min += 24*60

horas = duracao_min // 60
minutos = duracao_min % 60

print("O jogo durou", horas,"hora(s) e", minutos,"minuto(s).")
