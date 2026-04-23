#EXERCISE WHILE LOOP 2

def my_function():
    a = float(input("Enter Side A: "))
    b = float(input("Enter Side B: "))
    c = float(input("Enter Side C: "))
    if a + b <= c or a + c <= b or b + c <= a:
        print("Not a Triangle")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
        
    choice = input("Do you want to repeat? (Y/N): ")
    yes = "Y"
    
    while (True):
        if(choice == yes):
            my_function()
            continue
        else:
            print("Thank you for using my program ^^")
            break

my_function()