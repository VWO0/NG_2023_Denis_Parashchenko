print ("1. Convert from Celsius to Fahrenheit.")
print ("2. Convert from Fahrenheit to Celsius.")
operations = input("Select operations 1 or 2.")
operations = int(operations)

if operations == 1:
    celsius = float(input("Enter temperature in degrees Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print ("Result:",fahrenheit)

elif operations == 2:
    fahrenheit = float(input("Enter temperature in degrees Fahrenheit: "))
    celsius = (fahrenheit - 32) /1,8
    print ("Result:",celsius)

else:
    print ("Incorrect choice. Please enter 1 or 2.")