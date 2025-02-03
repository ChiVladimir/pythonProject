int_list = []
for i in range(101):
    int_list.append(i)
print(sum(int_list))

int_list_even = []
for i in range(2, 101, 2):
    int_list_even.append(i)
print(sum(int_list_even))

int_list_odd = []
for i in range(1, 101, 2):
    int_list_odd.append(i)
print(sum(int_list_odd))

x = int(input())
y = int(input())

print(x%y)


my_list = [1, 2, 3, 4, 5, 6]

print (my_list[::2])

