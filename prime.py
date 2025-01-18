num = int(input("Enter the number: "))
def prime(number):
    if number == 0 or number == 1:
        print("not prime")
    elif number > 1:
        for i in range(2, number):
            print(i)
            if number % i == 0:
                print(number, "is not prime")
                break

        else:
            print(number, "is prime")
    else:
        print(number, "is not prime")


prime(num)
