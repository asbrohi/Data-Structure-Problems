num = input("Enter the range of numbers to find armstrong numbers: ").split()

for i in range(int(num[0]), int(num[1])+1):
    n = str(i)
    l = len(n)
    arm = 0
    for j in n:
        arm += int(j)**l
        if arm == i:
            print(arm, end = " ")
    
