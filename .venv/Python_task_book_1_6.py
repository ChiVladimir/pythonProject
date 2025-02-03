
from typing import List, Any

my_list = [1, 2, 3, 4, 5]
print (sum(my_list))

my_list = [1, 2, 3, 4, 5]
my_sq_list: list[int] = []
for i in range(len(my_list)):
    my_sq_list.append(my_list[i] ** 2)
print (sum(my_sq_list))

my_list = [1, 2, 3, 4, 5]
my_sq_list: list[int] = []
for i in range(len(my_list)):
    my_sq_list.append(my_list[i] ** 0.5)
print (round(sum(my_sq_list), 2))

my_list = [1, 2, -3, 4, -5]
my_sep_list: list[int] = []
for i in range(len(my_list)):
    if my_list[i] > 0:
        my_sep_list.append(my_list[i])
print (sum(my_sep_list))

my_list = [-1, 2, -3, 4, 5, 11]
my_sep_list: list[int] = []
for i in range(len(my_list)):
    if 0 < my_list[i] < 10:
        my_sep_list.append(my_list[i])
print (sum(my_sep_list))


my_str = 'abcde'
for i in range(1, (len(my_str) + 1)):
    print (my_str[(-1 * i)])

