def fibbonacci(number):
    f0  =  0
    f1  =  1
    if number == 1:
        print(f0)
    elif number >= 2:
        print(f0,f1)
    f3 = 0
    for i in range (2, (number)):
        f3 = f0 +f1
        print(f3, end=" ")
        f0 = f1
        f1 = f3
    
num = int(input("Enter the number: "))
fibbonacci(num)