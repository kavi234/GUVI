#To calculate sum of digits of a number

n=int(input("enter number:"))
count=0
while(n>0):
    dig=n%10
    count=count+dig
    n=n//10
print(count)
