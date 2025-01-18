num = int(input("Enter the number: "))
def armstrong_number(number):
    digits = str(number)
    n = len(digits)
    new_number = 0
    for i in digits:
        new_number += int(i)**n
    if new_number == number:
        print("armstrong")
    else:
        print("not")
    
armstrong_number(num)