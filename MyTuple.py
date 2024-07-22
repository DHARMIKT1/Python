MyTuple = ("Apple","Mango","Banana")
print(MyTuple)
print("Using Index    : ",MyTuple[1])
print("Using Negative : ",MyTuple[-1])
print("Length is      : ",len(MyTuple))

print("-------------------------------------------------")

for x in MyTuple:
    print(x, end=" ")

for y in range(len(MyTuple)):
    print(MyTuple[y])

print("-------------------------------------------------")

print("Range data is : ",MyTuple[2:3])
print("Range data is : ",MyTuple[1:])
print("Range data is : ",MyTuple[:2])

print("-------------------------------------------------")

MyTuple = (1)
print("Type is : ",type(MyTuple))
MyTuple = (1, )
print("Type is : ",type(MyTuple))

print("-------------------------------------------------")

if "Apple" in MyTuple:
    print("Yes")
else:
    print("No")

print("-------------------------------------------------")

MyTuple = (1,2,3,4,5)
NewTuple = list(MyTuple)
NewTuple [1] = 6
print("After update : ",tuple(NewTuple))

print("-------------------------------------------------")

NewAddTuple = list(MyTuple)
NewAddTuple.append(10)
print("After added : ",NewAddTuple)

print("-------------------------------------------------")

SingleTuple = (11,)
MyTuple += SingleTuple
print("After Add : ",MyTuple)

print("-------------------------------------------------")

RemoveTuple = list(MyTuple)
RemoveTuple.remove(2)
print("After remove tuple : ",RemoveTuple)

print("-------------------------------------------------")

MyTuple = ("Apple","Mango","Banana","Orange")
(Red,Yellow,Green,Orange) = MyTuple
print(Red)
print(Yellow)
print(Green)
print(Orange)

print("-------------------------------------------------")

MyTuple = ("Apple","Mango","Banana","Orange")
(Red,Yellow,*Orange) = MyTuple
print(Red)
print(Yellow)
print(Orange)

print()

(Red,*Yellow,Orange) = MyTuple
print(Red)
print(Yellow)
print(Orange)

print("-------------------------------------------------")

fruits1 = ("Apple","Mango")
fruits2 = ("Banana","Orange")
fruits3 = fruits1 + fruits2
print(fruits3)

print()

fruits4 = fruits1 * 2
print(fruits4)

print()

print("Count is : ",fruits1.count("Mango"))
