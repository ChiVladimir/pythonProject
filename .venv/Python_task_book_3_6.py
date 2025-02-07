my_list = [1, 3, 44, 345, 67, 888, 9999]
res = []
for i in range(len(my_list)):
    if len(str(my_list[i])) != 3:
        res.append(my_list[i])
print(res)

num1 = "12345"
num2 = "12.34"
print(num1.isdigit())
print(num2.isdigit())

num = 1234500
flag = "no"
for i in range(len(str(num))):
    if int(str(num)[i]) == 0:
        flag = "yes"
print(flag)

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3]

difference = list(set(list1) - set(list2))
print(difference)


