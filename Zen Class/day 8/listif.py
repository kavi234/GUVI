a=["Arun","Sri","Kavi"]
b=["male","female","female"]
c=["married","married","single"]
for i in range(0,len(a)):
    if(b[i]=="male"):
        print("mr:",a[i])
    elif(c[i]=="single"):
        print("Ms:",a[i])
    else:
        print("Mrs:",a[i])
