#To count number of digits in a number

n=int(input("enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print(count)
