
def palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        print("string is palindrome")
    else:
        print("string is not palindrome")

s1 = input("Enter the string: ")
palindrome(s1)