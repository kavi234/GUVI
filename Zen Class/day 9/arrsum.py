#array sum: even index, even value

list=[15,20,35,40,55,60]
sum1=0
sum2=0
for i in range(0,len(list)):
    if(list[i]%2==0):
        sum1=sum1+list[i]
    elif(i%2==0):
        sum2=sum2+list[i]
print(sum1)
print(sum2)


