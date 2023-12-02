
def add(Number_1,Number_2):
    return Number_1+Number_2
def subtract(Number_1,Number_2):
    return Number_1-Number_2
def multiply(Number_1,Number_2):
    return Number_1*Number_2
def divide(Number_1, Number_2):
    try:
        result = Number_1 / Number_2
        return result
    except ZeroDivisionError:
        return "Divide by zero"


