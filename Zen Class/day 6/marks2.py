marks=[]
sum=0
for i in range(0,5):
    a=int(input())
    marks.append(a)
print(marks)
for i in range(0,len(marks)):
    sum=sum+marks[i]
print(sum)
percentage=((sum/500)*100)
print(percentage)
