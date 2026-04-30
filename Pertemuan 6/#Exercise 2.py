#Exercise 2
class Student:
    def __init__(self, name=None, score=None):
        self.name = name
        self.score = score

def main():
    obj = Student()
    
    while True:
        print("\n===== OOP Program =====")
        print("1. Declare Object")
        print("2. Display Object")
        print("3. Change Object Value")
        print("4. Delete Object")
        print("5. Exit Program")
        
        choice = input("Enter Your Choice (1/2/3/4/5): ")

        if choice == '1':
            obj.name = input("Enter Your Name: ")
            obj.score = input("Enter Your Score: ")
            print("Data Successfully Added")

        elif choice == '2':
            print("\nName: ", (obj.name))
            print("Score: ", (obj.score))

        elif choice == '3':
            change = input("What would you like to change (Name/Score): ")
            if change == "name":
                obj.name = input("Enter New Name: ")
                print("Name Data Successfully Changed")
            elif change == "score":
                obj.score = input("Enter New Score: ")
                print("Score Data Successfully Changed")
            else:
                print("Invalid Option")

        elif choice == '4':
            obj.name = None
            obj.score = None
            print("Data Successfully Deleted")

        elif choice == '5':
            print("Thank you for using my program.")
            break
        
        else:
            print("Invalid choice, please try again.")

main()