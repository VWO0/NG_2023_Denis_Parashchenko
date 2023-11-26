def Character_counting(Enter_file_name):
    Characters = {}
    try:
        with open(Enter_file_name,"r") as file:
            for line in file:
                for char in line:
                    if char in Characters:
                        Characters[char] += 1

                    else:
                        Characters[char] = 1
    except FileNotFoundError:
        print("File not found")
        return None
    return Characters

def Print_the_number_of_characters(Characters):
    if Characters is not None:
        print("Symbols and their number.")
        for char,count in Characters.items():
            print(f"{char}:{count}")


Enter_file_name = input("Enter file name(file_name.txt):")
result = Character_counting(Enter_file_name)
Print_the_number_of_characters(result)