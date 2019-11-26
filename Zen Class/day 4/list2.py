list1=input().split()
list2=[]
for a in list1:
	if a not in list2:
		list2.append(a)
print(list2)