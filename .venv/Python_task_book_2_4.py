my_str = 'rgib0hbiopwbrgibwrgv0wibvjwpib0pibpib pb '

for i in range(len(my_str)):
    if my_str[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print(i + 1)
        break

for i in range(len(my_str)):
    if my_str[i].isdigit():
        print(i + 1)
        break

my_num = 123456789
count = 0
for i in range(len(str(my_num))):
    if int(str(my_num)[i]) % 2 == 0:
        count += 1
print(count)

my_dict = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
}

list_of_keys = set(my_dict.keys())
print(sorted(list_of_keys))

my_str = 'abcde'
res_str = []
for i in range(len(my_str)):
    if i % 2 == 0:
        res_str.append(my_str[i].upper())
    else:
        res_str.append(my_str[i])

print("".join(res_str))

my_str = 'aaa bbb ccc'
res_str = my_str.split(' ')
for i in range(len(res_str)):
    res_str[i] = f"{res_str[i][0].upper()}{res_str[i][1:]}"
print(" ".join(res_str))


my_date = '2025-12-31'
list_4_split = my_date.split('-')
date_tuple = (list_4_split[2], list_4_split[1], list_4_split[0])
print(date_tuple)


