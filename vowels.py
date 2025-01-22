s1 = input("Input the string to see the consonanst and vowels: ")

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = [char for char in s1 if char.isalpha() and char.lower() not in vowels]
vow = [char for char in s1 if char.isalpha() and char.lower() in vowels]
print("Consonants: ", len(consonants), " Vowels: ", len(vow))