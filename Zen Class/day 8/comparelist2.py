a=[2,4,3,2,4]
b=[3,5,3,8,5]
c=[6,20,9,16,20]
count=0
for i in range(0,len(a)):
    if(a[i]*b[i]==c[i]):
        count=count+1
    else:
        break;
if(count ==len(a)):
    print("list are equal")
else:
    print("list are not equal")

