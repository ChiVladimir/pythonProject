
my_str = '023m0df0dfg0'

set_of_dgtpos = []

for i in range(len(my_str)):
    if my_str[i].isdigit():
        set_of_dgtpos.append(i + 1)
print (set_of_dgtpos)

my_str = 'AbCdE'
print (my_str.swapcase())

my_list = [1, 2, 3, 4, 5, 6]

res_list = []
for i in range(0, len(my_list), 2):
    res_list.append(f"{my_list[i]}{my_list[i + 1]}")
print(res_list)

my_str = 'aaa bbb ccc eee fff'

res_str = my_str.split(' ')
count = 1
for i in range(len(res_str)):
    if count%2 == 0:
        res_str[i] = f"{res_str[i][0].upper()}{res_str[i][1:]}"
    else:
        res_str[i] = f"{res_str[i]}"
    count += 1

print(" ".join(res_str))
