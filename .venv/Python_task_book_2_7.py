from curses.ascii import isupper

my_str = 'm'

if isupper(my_str): print ("Uppercase")
else: print ("Lowercase")

my_num = 123789
list_res = []
for i in range(len(str(my_num))):
    if int(str(my_num)[i])%2 == 0:
        list_res.append(str(my_num)[i])

print (int("".join(list_res)))


my_date_tuple = ('2025', '12', '31')
date_dict = {}
my_list = list(my_date_tuple)
my_dict = {'year':my_list[0], 'month':my_list[1], 'day':my_list[2]}

print("{")
for item in my_dict.items():
    print("     '",item[0], "': ", item[1], ",", sep='')
print("}")
