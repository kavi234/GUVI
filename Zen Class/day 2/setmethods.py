set={"apple","banana","cherry"}
set2={"google","microsoft","apple"}

set.add("orange")
print(set)

set3=set.symmetric_difference(set2)
print(set3)

set.symmetric_difference_update(set2)
print(set)

set3=set.union(set2)
print(set3)

set.update(set2)
print(set)

set3=set.difference(set2)
print(set3)

set.difference_update(set2)
print(set)

set.discard("banana")
print(set)

set3=set.intersection(set2)
print(set3)

set.intersection_update(set2)
print(set)

set3=set.isdisjoint(set2)
print(set3)

set3=set.issubset(set2)
print(set3)

set3=set.issuperset(set2)
print(set3)

set2.pop()
print(set2)

set2.remove("apple")
print(set2)

set2.clear()
print(set2)






