#Exercise 1
class Student:
    "Student Biodata"
    
    def __init__(self):
        self.name = ""
        self.age = 0
        self.number = ""
        self.group = ""
    
    def get_biodata(self):
        print("--- Enter Student Biodata ---")
        self.name = (input("Enter Name: "))
        self.age = int(input("Enter Age: "))
        self.number = int(input("Enter Number: "))
        self.group = (input("Enter Group: "))
        
    def display_biodata(self):
        print("--- Student Biodata Report ---")
        print("Name: ", (self.name))
        print("Age: ", (self.age))
        print("Number: ", (self.number))
        print("Group: ", (self.group))
        
student_obj = Student()
student_obj.get_biodata()
student_obj.display_biodata()