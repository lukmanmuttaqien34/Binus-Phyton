#EXERCISE WHILE LOOP 1

def my_function():
    num = int(input("Enter any number: "))
    if(num % 2 == 0):
        print("The number" + " " + str(num) + " " +  "is even")
    else:
        print("The number" + " " + str(num) + " " + "is odd")
        
    choice = input("Do you want to repeat? (Y/N): ")
    yes = "Y"
    
    while(True):
        if(choice == yes):
            my_function()
            continue
        else:
            print("Thank you for using my program ^^")
            break

my_function()