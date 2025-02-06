my_str = "аждая буква величиною в метр и арисована асляной аской!"

my_list = my_str.split(' ')
list_res = []

for i in range(len(my_list)):
    if my_list[i][0] == "а":
        list_res.append(my_list[i])

print (list_res)

my_list_nums = [1,3,5,7,-9,5,7,3,9]
flag = True
for i in range(len(my_list_nums)):
    if my_list_nums[i] < 0:
        flag = False

print (flag)

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

overlap = set(lst1) & set(lst2)
print(list(overlap))

my_str = ""
num = 5
for i in range(num):
    my_str = f"{my_str}{"0"}"

print(my_str)
