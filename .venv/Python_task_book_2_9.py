from curses.ascii import isupper

list_res = []
for i in range(0, 101, 2):
    list_res.append(i)

print (list_res)

my_list = ['1', '2', '3', '4', '5']

print ([int(my_list[i]) for i in range(len(my_list) - 1, -1, -1)])

txt1 = 'abcde'
txt2 = '12345'
my_dict = {}

for i in range(len(txt1)):
    my_dict[txt1[i]] = txt2[i]

print("{")
for item in my_dict.items():
    print("     '",item[0], "': ", item[1], ",", sep='')
print("}")

