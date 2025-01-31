x = int(input())

print (f"The first digit of the number {x} is {str(x)[0]}")

print (f"The last digit of the number {x} is {str(x)[-1]}")

print (f"The sum of the first and last digit of the number {x} is {int(str(x)[0]) + int(str(x)[-1])}")

print (f"The length of the number {x} is {len(str(x))}")

y = int(input())
if str(x)[0] == str(y)[0]:
    print(f"The first symbols of the numbers {str(x)} and {str(y)} are the same")
else:
     print(f"The first symbols of the numbers {str(x)} and {str(y)} is not the same")


my_list = [1, 2, 3, 4, 5, 6]

print (my_list[0:3])

