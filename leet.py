def noumber(n):
    j=n
    no=0
    set1=set()
    flag=1
    if(n==1):
        return True
    if(n>1):
        while(j!=1): 
            no=0  
            while(j>0 ):
                d=j%10
                no=no+(d**2)
                
                j=int(j/10)
            j=no
            if(no not in set1):
            
                set1.add(no)
            else:
                flag=0
                break
            

        print(set1)
        if(flag==1):
            return (True)
        if(flag==0):
            return (False)



   

           
            
        



var=int(input(''))
print(noumber(var))

