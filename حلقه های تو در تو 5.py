m=0
for i in range (10):
    a=int(input())
    while (a!=0):
        b=a%10
        a=a/10
        m=m+b
print(m)
