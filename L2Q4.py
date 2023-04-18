a, b = input().split()
a = int(a)
b = int(b)
c = int(a+1)

if (b == 0):
    print(a, b, "errados") 
elif (a == b) or (b == c):
    print(a, b, "ok")
else:
    print(a, b, "errados")