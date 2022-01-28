#search_for_nth_element
# 6
# 2,3,4,5,3,6
#3
#2
#output   4

#code
length=int(input(''))
arr=list(map(int,input().split(',')))
key=int(input(''))
occurence_value=int(input(''))

count=0
flag=0
for i in range(0,len(arr)):
    if(arr[i]==key and count==occurence_value-1):
        print(i)
        flag=1
        break
    elif(arr[i]==key and count<occurence_value-1):
        count=count+1
    else:
        i=i+1
if(flag==0):
    print('-1')
  


#code

#Given string str, a character ch, and a value N, the task is to find the index of the Nth occurrence of the given character in the given string. Print -1 if no such occurrence exists.
"""Input: str = “Geeks”, ch = ‘e’, N = 2 
Output: 2

Input: str = “GFG”, ch = ‘e’, N = 2 
Output: -1 """
sentence=str(input(''))
word=str(input(''))
occurence_val=int(input(''))
count=0
i=0
flag=0
while(i<len(sentence)):
    if(sentence[i]==word and count==occurence_val-1):
        flag=1
        print(i)
        break
    elif(sentence[i]==word and count<occurence_val):
       
        count=count+1
        i=i+1
    else:
        
        i=i+1
if(flag==0):
    print(-1)
    
        
