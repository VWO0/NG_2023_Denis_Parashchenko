def celsius_to_fahrenheit(data):
    return data * 1.8 + 32

def fahrenheit_to_celsius(data):
    return (data - 32) / 1.8

print("1. Convert from Celsius to Fahrenheit.","2. Convert from Fahrenheit to Celsius.")
operation = input("Select operation 1 or 2: ")
data =float(input("Enter temperature"))
if operation == '1':
    result = celsius_to_fahrenheit(celsius)
    print(f"Result: {result}°F")

elif operation == '2':
    result = fahrenheit_to_celsius(fahrenheit)
    print(f"Result: {result}°C")

else:
    print("Incorrect choice. Please enter 1 or 2.")
