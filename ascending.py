arr  = input("Enter numbers separated by spaces: ").split()

for _ in range(len(arr)):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

print(arr)

    

 
        