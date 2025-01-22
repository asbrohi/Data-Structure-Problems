num = int(input("Enter the number to find factorial: "))

def factorial(number):
    result = 1
    if number <= 0:
        print("Input the number more than 0")
    else:
        for i in range (number, 1, -1):
            result *=i
        print(f"Factorial of {number} is {result}")   
    
factorial(num)
