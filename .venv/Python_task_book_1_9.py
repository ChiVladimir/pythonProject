
my_str = 'abcdef'

print (my_str[3:])


my_dict = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
}
print("{")
for item in my_dict.items():
    my_dict[item[0]] = int(item[1]) * 2
    print("     '",item[0], "': ", my_dict[item[0]], ",", sep='')
print("}")
