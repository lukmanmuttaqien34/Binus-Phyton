#program to determine the solutions of a quadratic equation using the discriminant

import math
a = float(input("Value A: "))
b = float(input("Value B: "))
c = float(input("Value C: "))
discriminant = b**2 - 4*a*c
equation = f"{a}x² + {b}x + {c} = 0"

if a == 0:
    print("It is not a quadratic equation")
else:
    if discriminant > 0:
        print("It has distinct roots")
        print(f"The quadratic equation is: {equation}")
        print(f"The discriminant value is: {discriminant}")
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"The value of root x1 is: {x1}")
        print(f"The value of root x2 is: {x2}")
        
    elif discriminant < 0:
        print("It has imaginary roots")
        print(f"The quadratic equation is: {equation}")
        print(f"The discriminant value is: {discriminant}")
        print("The formulas for roots x1 and x2 are: (-b ± sqrt(discriminant)) / 2a")
        
    else:
        print("It has a double root")
        print(f"The quadratic equation is: {equation}")
        print(f"The discriminant value is: {discriminant}")
        x = -b / (2*a)
        print(f"The root value is: {x}")