# Write your code here
n=int(input())
while(n):
	word=str(input())
	print(word)
	i=0
	j=len(word)-1
	flag=0
	while(i<j and i!=j):
		if(word[i]==word[j]):
			print(word[i],word[j])
			i=i+1
			j=j-1
			
			
		else:
			print(word[i],word[j])
			flag=1
			print("False")
			break
	if(flag!=1):
		print("True")
	n=n-1