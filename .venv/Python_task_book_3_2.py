my_numbers = [x for x in range(1, 11, 2)]
print(my_numbers)


tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)

tpl3 = tpl1 + tpl2
print(tpl1 + tpl2)

dct1 = {
	'a': 1,
	'b': 2,
}
dct2 = {
	'c': 3,
	'd': 4,
}

dct3 = dct1
dct3.update(dct2)

print("{")
for item in dct3.items():
    print("     '",item[0], "': ", item[1], ",", sep='')
print("}")



my_list = [1, 2, 3, 4, 5, 6]
res_list_1 = []
res_list_2 = []
for i in range(len(my_list)):
    if i < int(len(my_list)/2):
        res_list_1.append(my_list[i])
    else:
        res_list_2.append(my_list[i])
print(sum(res_list_1) / sum(res_list_2))
