set1 = set(input("Enter the elements of the third set separated by spaces: ").split())
set2 = set(input("Enter the elements of the third set separated by spaces: ").split())
set3 = set(input("Enter the elements of the third set separated by spaces: ").split())
common_set = set1 & set2 & set3
result_set = common_set | set1 | set2 | set3
print("A set of non-unique elements:", result_set)