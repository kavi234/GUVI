sum=0
marks=list()
for i in range(0,5):
    num=int(input("enter marks%d" %i))
    marks.append(num)
    sum=sum+marks[i]
print(sum)
avg=sum/5
print(avg)