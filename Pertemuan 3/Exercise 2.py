#categorize the age input provided by the user 
age = int (input ("age: "))
if ( age < 0 ) :
    print("not applicable")
elif ( ( age >= 0 ) and ( age <= 1 ) ):
    print("baby")
elif ( ( age >= 2 ) and ( age <= 3 ) ):
    print("toddler")
elif ( ( age >= 4 ) and ( age <= 5 ) ):
    print("preschooler")
elif ( ( age >= 6 ) and ( age <= 12 ) ):
    print("child")   
elif ( ( age >= 13 ) and ( age <= 17 ) ):
    print("teenager")
elif ( ( age >= 18 ) and ( age <= 21 ) ):
    print("young adult")
elif ( ( age >= 22 ) and ( age <= 30 ) ):
    print("pre adult")
elif ( ( age >= 31 ) and ( age <= 50 ) ):
    print("adult")   
elif ( ( age >= 51 ) and ( age <= 70 ) ):
    print("pre elderly")  
else :
    print("elderly")    