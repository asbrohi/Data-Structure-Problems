input_string = input("Enter numbers separated by spaces: ")
input_list = input_string.split()
largest = int(input_list[0])
smallest = int(input_list[0])
for i in input_list:
    if int(i) > largest:
        largest = int(i)
    elif int(i) < smallest:
        smallest = int(i)
print(f'The smallest number is: {smallest}')
print(f'The largest number is: {largest}')