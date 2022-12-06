n=int(input("Enter the value. "))#
ans=0
while(n!=0):
	digit=n%10 #23%10=3
	ans=ans+digit
	n=n//10 #int(n/10)
print("ANSWER = ",ans)
