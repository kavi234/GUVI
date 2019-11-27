a=[2,4,3,2,4]
b=[3,5,3,8,5]
c=[6,20,9,16,20]
match="true"
for i in range(0,len(a)):
    if(a[i]*b[i]!=c[i]):
        print("list are not equal")
        match="false"
        break
if(match!="false"):
    print("list are equal")
