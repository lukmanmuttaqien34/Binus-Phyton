#Function Exercise

def id_ku(): 
    print("---------------------------------")
    print("|           si tampan           |")
    print("|               |               |")
    print("|               |               |")
    print("|          pondok aren          |")
    print("---------------------------------")


    menu = input("Enter Menu (+|-|/|*|%|stop)= ")
    value_1 = int(input("Value 1 = "))
    value_2 = int(input("Value 2 = "))
    resultAdd = int(value_1 + value_2)
    resultSub = int(value_1 - value_2)
    resultDiv = int(value_1 / value_2)
    resultMul = int(value_1 * value_2)
    resultMod = int(value_1 % value_2)
    add = "+"
    sub = "-"
    div = "/"
    mul = "*"
    mod = "%"

    if menu == "+":
        print("The result of addition" + " " + str(value_1) + " " + "+" + " " + str(value_2) + " " + "is" + " " + str(resultAdd))
    elif menu == "-":
        print("The result of substraction" + " " + str(value_1) +   " " + "-" + " " + str(value_2) + " " + "is" + " " + str(resultSub))
    elif menu == "/":
        print("The result of division" + " " + str(value_1) +   " " + "/" + " " + str(value_2) + " " + "is" + " " + str(resultDiv))
    elif menu == "*":
        print("The result of multiplication" + " " + str(value_1) +   " " + "*" + " " + str(value_2) + " " + "is" + " " + str(resultMul))
    elif menu == "%":
        print("The result of modulus" + " " + str(value_1) +   " " + "%" + " " + str(value_2) + " " + "is" + " " + str(resultMod))
    else:
        print("Thank you for using my program.")
    
    while(True):
        if(menu == "+","-","/","*","%"):
            id_ku()

id_ku() 