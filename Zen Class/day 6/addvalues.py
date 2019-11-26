a=[10,20,81,91,50,52,55]
for i in range(0,len(a)):
    if(a[i]>80):
        a[i]=a[i]+10
    else:
        a[i]=a[i]+5
print(a)
