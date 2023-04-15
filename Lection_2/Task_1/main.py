n = int(input("Enter the number of elements: "))
elements = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")    
    elements.append(element)

element_to_count = input("Enter an element to count: ")
count = elements.count(element_to_count)

print(f"Number of items entered '{element_to_count}': {count}")
