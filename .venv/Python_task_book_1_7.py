my_dict = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
}
list_of_values = []
for v in my_dict.values():
    list_of_values.append(v)

print(sum(list_of_values))

list_of_values = []
for v in my_dict.values():
    list_of_values.append(v ** 2)

print(sum(list_of_values))

my_str = 'abcde'
list_from_str = []
for i in range(len(my_str)):
    list_from_str.append(my_str[i])

print (list_from_str)

my_number = 12345
list_from_num = []
for i in range(len(str(my_number))):
    list_from_num.append(str(my_number)[i])

print (list_from_num)

list_from_num = []
for i in range(1, (1 + len(str(my_number)))):
    list_from_num.append(str(my_number)[-1 * i])

print (int("".join(list_from_num)))

list_from_num = []
for i in range(len(str(my_number))):
    list_from_num.append(int(str(my_number)[i]))

print (sum(list_from_num))

