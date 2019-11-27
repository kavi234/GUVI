a=int(input("enter a number:"))
b=[10,20,30]
found=False
for i in range(0,len(b)):
    if(b[i]==a):
        found=True
        break
if(found==False):
    print("Match Not Found")
else:
    print("Match Found")


    
        
