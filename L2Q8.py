L1 = float(input())
L2 = float(input())
L3 = float(input())

a = max(L1, L2, L3)
c = min(L1, L2, L3)
b = (L1 + L2 + L3) - a - c

if(a>=(b+c)):
    print("NAO FORMA TRIANGULO")
elif((a*a) == ((b*b) + (c*c))):
    print("TRIANGULO RETANGULO")
elif(a==b) and (b==c):
    print("TRIANGULO EQUILATERO")
elif(a==b) or (b==c) or (a==c):
    print("TRIANGULO ISOSCELES")
elif(a!=b) or (a!=c):
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")      