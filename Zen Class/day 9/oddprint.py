#To print all odd number between 1 to n

num=int(input("enter a number:"))
for i in range(0,num+1):
    if(i%2!=0):
        print(i)
