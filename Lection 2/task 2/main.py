Data = list(input("Enter data"))
Numbers = [char for char in Data if char.isdigit()]
Counting_numbers = len(Numbers)
Other_characters = [char for char in Data if not char.isdigit()]
Counting_other_characters = len(Other_characters)
print("User data list: ",Data)
print("Numbers: ",Numbers,"Counting numbers: ",Counting_numbers)
print("Other characters: ", Other_characters,"Counting other characters: ",Counting_other_characters)