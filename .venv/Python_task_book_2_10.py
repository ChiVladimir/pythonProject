my_str = "Naughty to 100 in 4.9 seconds. That's great! V"
count = 0
for i in range(len(my_str)):
    if not my_str[i].isdigit():
        count += 1
        if count > 3:
            print ("Letters are gonna bust!")
            break

my_num = 123789

print ([int(str(my_num)[i]) for i in range(len(str(my_num)) - 1, -1, -1) if int(str(my_num)[i]) % 2 == 0])


my_str = 'abcde abcde abcde'

res_str = my_str.split(' ')
for i in range(len(res_str)):
    res_str[i] = f"!{res_str[i][1:]}"

print(" ".join(res_str))

my_list = ['1', '2', '3', '4', '5']

print(sum([int(my_list[i]) for i in range(len(my_list))]))