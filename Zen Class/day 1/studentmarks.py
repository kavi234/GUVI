f=int(input("Enter no.of students: "))
for i in range(0,f):
    mark1=int(input())
    mark2=int(input())
    mark3=int(input())
    mark4=int(input())
    mark5=int(input())
    tot=mark1+mark2+mark3+mark4+mark5
    avg=float(tot/5)
    percentage=float((avg/100)*100)
    print(tot)
    print(avg)
    print(percentage)
    if(percentage>90):
        print("A Grade")
    elif(percentage>80):
        print("B Grade")
    elif(percentage>70):
        print("C Grade")
    elif(percentage>60):
        print("D Grade")
    else:
        print("E Grade")
        