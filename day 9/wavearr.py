#wave array

list=[1,4,2,8,5,11]
j=0
for i in range(0,(len(list)-2),2):
    if(list[i]<list[i+1] and list[i+1]>list[i+2]):
        j+=1
        if(j==len(list)//3):
            print(True)
    else:
        print(False)
    
        
