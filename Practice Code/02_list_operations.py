lst = ["apple","Mango", "Cherray"]
print (lst)

lst = ["apple","Mango","Cherray","apple"]
print(lst)
print(lst[1])
print("Length is:",lst)

for x in range(len(lst)):
    print(x, end=" ")

print("\n----------------------------------------")

for y in range(len(lst)):
    print(lst[y], end=" ")

print("\n----------------------------------------")

lst = list((1,2,3,4,5,6))
print(lst)
print("Range data is  :",lst[2:5])
print("Last index is  :",lst[:4])
print("First index is :",lst[:2])

if 1 in lst:
    print("Yes")
else:
    print("No")

lst[1] = 45
print("After change :",lst)

lst[1:3] = [46,47]
print("After range modification :",lst)

lst.insert(2,56)
print("After insert method :",lst)

lst.append(100)
print("After append method :",lst)

lst = [1,2,3]
lst2 = [4,5,6]
lst.extend(lst2)
print("After extend method :",lst)

thisTuple = (7,8,9)
lst.extend(thisTuple)
print("After extend tuple is :",lst)

lst.remove(1)
print("After remove method :",lst)

lst.pop(3)
print("After POP method :",lst)

lst = [4,5,6,8,9,7,1,3,2]
lst.sort()
print("After sort method :",lst)
lst.sort(reverse = True)
print("After decending :",lst)


MyList = list(lst)
print("Copy using constructor :",MyList)
print("Count is :",lst.count(2))
