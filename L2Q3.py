cargo = input()
tempo = int(input())
salario_atual = float(input())

if salario_atual >=1039:
    if cargo == 'Gerente':
        reajuste1 = 0.12
        reajuste2 = 0.13
        reajuste3 = 0.15
    elif cargo == 'Engenheiro':
        reajuste1 = 0.07
        reajuste2 = 0.11
        reajuste3 = 0.14
    else:
        reajuste1 = 0.05
        reajuste2 = 0.05
        reajuste3 = 0.05
    if (tempo>0) and (tempo<=3):
        reajuste = reajuste1
    elif (tempo>3) and (tempo<=6):
        reajuste = reajuste2
    else:
        reajuste = reajuste3    
    salario_novo = (salario_atual*reajuste) + salario_atual
    print("%.2f"%(salario_atual*reajuste))
    print("%.2f"%salario_novo)
else:
    print("Salário inválido!")    