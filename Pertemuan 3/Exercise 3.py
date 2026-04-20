#program to perform temperature conversions

print ("1: Celsius to Fahrenheit")
print ("2: Celsius to Kelvin")
print ("3: Fahrenheit to Celsius")
print ("4: Fahrenheit to Kelvin")
print ("5: Kelvin to Celsius")
print ("6: Kelvin to Fahrenheit")
    
choice = input ("Select conversion (1-6): ")
temp = float (input ("Enter temperature: "))

if choice == '1':
    print (f"{temp}°C = {(temp * 9/5) + 32:.2f}°F")
elif choice == '2':
    print (f"{temp}°C = {temp + 273.15:.2f}K")
elif choice == '3':
    print (f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
elif choice == '4':
    print (f"{temp}°F = {(temp - 32) * 5/9 + 273.15:.2f}K")
elif choice == '5':
    print (f"{temp}K = {temp - 273.15:.2f}°C")
elif choice == '6':
    print (f"{temp}K = {(temp - 273.15) * 9/5 + 32:.2f}°F")
else:
    print ("not applicable")