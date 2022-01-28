# 2 positive integers given m and n
# find the sum of all numbers divisible by both 3 and 5

m=int(input(''))
n=int(input(''))
sum=0
for i in range(m,n+1):
    if(i%15==0):
        sum=sum+i
print(sum)