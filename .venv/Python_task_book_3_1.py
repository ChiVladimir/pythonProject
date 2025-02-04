my_numbers = [x for x in range(1, 7)]
print(my_numbers)


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = lst1 + lst2
print(lst3)

my_list = [1, 2, 3, 4, 5, 6]
res_list = []
for i in range(int(len(my_list)/2)):
    res_list.append(my_list[i])

print(sum(res_list))
