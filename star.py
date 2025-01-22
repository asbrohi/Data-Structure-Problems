num = int(input("Enter the number of rows you want to print: "))
shape = input("Enter the shape you want to print: ")


def pattern(number, shape):
    shape = shape.lower()
    if shape == "pyramid":
        for i in range(0, number):
            print(" "*(number-i), "*"*((2*i+1)))
    elif shape == "diamond":
        for i in range(0, number):
            print(" " * (number - i), "*" * ((2 * i + 1)))
        for j in range(number, 0, -1):
            print(" " * (number - j), "*" * ((2 * j - 1)))

pattern(num, shape)