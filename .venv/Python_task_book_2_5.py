

my_str = '023m0df0dfg0'

set_of_zeros = set()
for i in range(len(my_str)):
    if my_str[i] == '0':
        set_of_zeros.add(i)
print (set_of_zeros)

my_str = 'abcdefg'
res_str = []
i = 1
for i in range(len(my_str) + 1):
    if i % 3 == 0:
        continue
    else:
        res_str.append(my_str[i - 1])

print("".join(res_str))

my_list = [1, 2, 3, 4, 5, 6]

my_neg_list = []
my_pos_list = []
for i in range(len(my_list)):
    if my_list[i]%2 == 0:
        my_pos_list.append(my_list[i])
    else:
        my_neg_list.append(my_list[i])
print (sum(my_pos_list), sum(my_neg_list), sum(my_pos_list)/sum(my_neg_list))



my_date = ['2025', '12', '31']
date_tuple = (my_date[2], my_date[1], my_date[0])
print(date_tuple)


