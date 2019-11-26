marks=[100,100,30,40,50,60,90,95,99]
marks1=[]
'''for i in range(0,len(marks)):
    a=int(input())
    marks.append(a)
print(marks)'''

for i in range(0,len(marks)):
    if(marks[i]>90):
        marks1.append(marks[i])
print(marks1)

        




