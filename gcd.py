n1 = int(input("Input the first no: "))
n2 = int(input("Input the second no: "))

def gcd(n1, n2):
    if n1 > n2:
        while n2 != 0:
            r = n1%n2
            n1 = n2
            n2 = r
        print(n1)
    elif n2 > n1:
        while n1 != 0:
            r = n2%n1
            n2 = n1
            n1 = r
        print(n2)

gcd(n1, n2)