arr = input("Enter numbers separated by spaces: ").split()
sum = 0
for i in range(0, len(arr)):
    sum +=int(arr[i])
print(sum)