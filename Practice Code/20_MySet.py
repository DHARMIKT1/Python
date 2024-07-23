MySet = {1,2,3}
print(MySet)

print("--------------------------------------------------")

MySet = set((1,2,3,4,5))
print("Using constructor : ",MySet)

print("--------------------------------------------------")

for x in MySet:
    #print(MySet)
    print(x)

print("--------------------------------------------------")

if 3 in MySet:
    print("Yes")
else:
    print("No")

print("--------------------------------------------------")

MySet.add(6)
print("After add : ",MySet)

print("--------------------------------------------------")

NewSet = (7,8)
MySet.update(NewSet)
print("After update : ",MySet)

print("--------------------------------------------------")

MySet.remove(3)
print("After remove method : ",MySet)

print("--------------------------------------------------")

MySet.discard(4)
print("After discard method : ",MySet)

print("--------------------------------------------------")

MySet.pop() #Remove an item randomly
print("After pop method1 : ",MySet)

print("--------------------------------------------------")

MySet.pop() #Remove an item randomly
print("After pop method2 : ",MySet)

print("--------------------------------------------------")

MySet.clear()

del MySet

Set1 = {1,2,3}
Set2 = {3,4,5}
Set3 = Set1.union(Set2)
print("After using union method : ",Set3)

print("--------------------------------------------------")

Set3 = Set1 | Set2
print("After using pipe sign : ",Set3)

print("--------------------------------------------------")

Set1 = {1,2,3}
Set2 = {3,4,5}
Set3 = Set1.intersection(Set2)
print("After intersection : ",Set3)

print("--------------------------------------------------")

Set3 = Set1 & Set2
print("After and operator : ",Set3)

print("--------------------------------------------------")

Set1.intersection_update(Set2)
print("Intersection update is : ",Set1)

print("--------------------------------------------------")

Set4 = (True,1)
print(Set4)

print("--------------------------------------------------")

Set1 = {1,2,3}
Set2 = {3,4,5}
Set3 = Set1.difference(Set2)
print("Difference is : ",Set3)

print("--------------------------------------------------")

Set3 = Set1 - Set2
print("Minus is : ",Set3)

print("--------------------------------------------------")

Set1.difference_update(Set2)
print("Difference update : ",Set1)

print("--------------------------------------------------")

Set1 = {1,2,3}
Set2 = {3,4,5}
Set3 = Set1.symmetric_difference(Set2)
print("Symmetric difference : ",Set3)

print("--------------------------------------------------")

Set3 = Set1 ^ Set2
print(Set3)

print("--------------------------------------------------")

Set1 = {1,2,3}
Set2 = {3,4,5}
Set3 = Set1.union(Set2)
print(Set3)
