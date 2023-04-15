n = int(input("Введите количество элементов: "))
elements = []
for i in range(n):
    element = input(f"Введите элемент {i+1}: ")    
    elements.append(element)

element_to_count = input("Введите элемент для подсчета: ")
count = elements.count(element_to_count)

print(f"Количество введенных элементов '{element_to_count}': {count}")