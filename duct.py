duct=dict([])
print(type(duct))
print(duct)
n=int(input())
while(n):
    b=list(map(str,input().split()))
    duct[b[0]]=b[1]
    n=n-1
print(duct) 
for i in duct:
    print(duct.get(i))
    d=duct.get(i)
    print(d,type(d))
    if(float(d)>98.6):
        print(i)