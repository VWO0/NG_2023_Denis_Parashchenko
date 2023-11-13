Data = list(input("Enter data"))
Vowel_list = "AEIOUaeiou"
Vowel_letters = []
for char in Data:
    if char in Vowel_list:
        Vowel_letters += char


print("User data list: ",Data)
print("Vowel letters: ",Vowel_letters)