from curses.ascii import isupper

list_res = []
for i in range(1, 11):
    list_res.append(i)

print (list_res)


my_str = "Naughty to 100 in 4.9 seconds. That's great! V"
count = 0
for i in range(len(my_str)):
    if isupper(my_str[i]):
        count += 1
        if count > 2: print ("Capital letters are gonna bust!")


my_list = ['1', '2', '3', '4', '5']

print ([int(my_list[i]) for i in range(len(my_list))])