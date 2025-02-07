my_list = [1, 3, 44, 345, 67, 888, 9999]
res = []
for i in range(len(my_list)):
    print ("3" in str(my_list[i]))

my_str = "1, 3, 44, 345, 67, 888, 9999"

print((sorted((my_str.split(", ")), reverse=True))[0])



my_str = 'kebab-case'

res_str = my_str.split('-')

print("_".join(res_str))
#
# txt1 = '12345'
# txt2 = '45678'
#
# print(list(txt1))
# overlap = set(list(txt1)) & set(list(txt2))
# print("".join(sorted(overlap)))
#
# my_str = 'a bc def ghij'
# res = []
#
# for i in range(len(my_str.split(' '))):
#     if len(my_str.split(' ')[i]) <= 3:
#         res.append(my_str.split(' ')[i].upper())
#     else: res.append(my_str.split(' ')[i])
# print(" ".join(res))

# my_list = [1, 3, 44, 345, 67, 888, 9999]
# res = []
# for i in range(len(my_list)):
#     if len(str(my_list[i])) != 3:
#         res.append(my_list[i])
# print(res)
#
# num1 = "12345"
# num2 = "12.34"
# print(num1.isdigit())
# print(num2.isdigit())
#
# num = 1234500
# flag = "no"
# for i in range(len(str(num))):
#     if int(str(num)[i]) == 0:
#         flag = "yes"
# print(flag)
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 2, 3]
#
# difference = list(set(list1) - set(list2))
# print(difference)


