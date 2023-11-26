def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

print("1. Convert from Celsius to Fahrenheit.")
print("2. Convert from Fahrenheit to Celsius.")
operation = input("Select operation 1 or 2: ")

if operation == '1':
    celsius = float(input("Enter temperature in degrees Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print(f"Result: {result}°F")

elif operation == '2':
    fahrenheit = float(input("Enter temperature in degrees Fahrenheit: "))
    result = fahrenheit_to_celsius(fahrenheit)
    print(f"Result: {result}°C")

else:
    print("Incorrect choice. Please enter 1 or 2.")
