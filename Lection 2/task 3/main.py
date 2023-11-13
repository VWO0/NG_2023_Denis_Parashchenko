import pandas as pd

Enter_number = int(input("Enter numbers."))

data = []
for i in range(1,Enter_number + 1):
    divisors = [j for j in range(1, i + 1) if i % j == 0]
    data.append ([i,divisors])
df = pd.DataFrame(data, columns=["Number", "Dividers"])
print(df)
#Finding Prime Numbers
prime_numbers = []
for i in range(2, Enter_number + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
if Enter_number >= 2:
    prime_numbers.append(Enter_number)
print("Prime numbers: ", prime_numbers)