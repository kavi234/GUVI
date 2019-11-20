list1=["apple","banana","cherry"]
list2=["ford","bmw","volvo"]
list1.append(list2)
print(list1)

list3=list1.copy()
print(list3)

list4=list1.count("cherry")
print(list4)

list5=list1.index("cherry")
print(list5)

list1.insert(1,"grapes")
print(list1)

list1.reverse()
print(list1)

list2.sort()
print(list2)

list1.extend(list2)
print(list1)

list1.pop(1)
print(list1)

list1.remove("banana")
print(list1)

list1.clear()
print(list1)



