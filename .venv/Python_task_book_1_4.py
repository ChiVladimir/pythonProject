y_Y = str(input())

if len(y_Y) > 1:
    print (f"Before last symbol of the string {y_Y} is {y_Y[-2]}")
else:
    print(f"The length of the string {y_Y} less then 1")

x = int(input())
y = int(input())

if x%y == 0:
    print("divided")
else:
    print("not divided")

my_str = 'abcde'

my_list = []

for i in range(len(my_str)):
    my_list.append(my_str[i])

print (my_list)

my_list = [1, 2, 3, 4, 5, 6]

print (my_list[2:5])

my_dict = {
	'year' : '2025',
	'month': '12',
	'day'  : '31',
}

print (f"{my_dict['year']}-{my_dict['month']}-{my_dict['day']}")