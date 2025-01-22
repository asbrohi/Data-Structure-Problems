x = input("Enter the string to reverse: ")
z=""
for i in range(len(x)-1, -1,-1):
	z +=x[i]
print(f'Reverse of {x} is: {z}')