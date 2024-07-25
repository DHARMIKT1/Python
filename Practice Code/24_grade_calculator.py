marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A")
elif 80 <= marks < 90:
    print("B")
elif 70 <= marks < 80:
    print("C")
elif 60 <= marks < 70:
    print("D")
elif 50 <= marks < 60:
    print("E")
else:
    print("Failed")
