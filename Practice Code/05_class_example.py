class MyClass:
	classVar = 1

	def __init__(self, inVar):
		self.inVar = inVar

obj1 = MyClass("Dharmik")
obj2 = MyClass("Tank")

print("Before Changing : ")
print(obj1.classVar, obj1.inVar)

MyClass.classVar = 2

obj1.inVar = "Rohini"

print("After Changing : ")
print(obj1.classVar, obj1.inVar)
