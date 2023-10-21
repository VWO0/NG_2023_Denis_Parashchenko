import Internal_files_for_the_calculator

Number_1 = float(input("Enter the first number: "))
Number_2 = float(input("Enter the second number: "))

Operations = {
    '+': Internal_files_for_the_calculator.add,
    '-': Internal_files_for_the_calculator.subtract,
    '*': Internal_files_for_the_calculator.multiply,
    '/': Internal_files_for_the_calculator.divide
}

Operation = input("Select operation (+, -, *, /): ")

try:
    result = Operations[Operation](Number_1, Number_2)
    print("Result:", result)
except KeyError:
    print("Invalid operation selected. Please choose from +, -, *, or /.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", e)