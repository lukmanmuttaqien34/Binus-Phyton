#program to determine the type of triangle

a = float (input ("A: "))
b = float (input ("B: "))
c = float (input ("C: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Not a Triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")