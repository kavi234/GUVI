#sum of all even numbers 1 to n

num=int(input("enter a number:"))
sum=0
for i in range(0,num+1):
    if(i%2==0):
        sum=sum+i
        print(sum)
