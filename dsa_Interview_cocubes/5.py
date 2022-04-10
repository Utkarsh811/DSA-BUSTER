origno=int(input())
origno=str(origno)
print(type(origno))
new=''
for i in range(1,len(origno)):
    if(i%2!=0):
        d=int(origno[i])**2
        new=new+str(d)
        

print(new)
print(new[0:4])
