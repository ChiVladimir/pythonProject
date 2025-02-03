word_1 = "vfljwhbwfvjlhbfv"
word_2 = "hgbigbibgwjbgnvz"
if word_1[0] == word_2[-1]:
    print ("There's a match!")
else:
    print("There's not match!")

my_str = 'rgib0hbiopwbrgibwrgv0wibvjwpib0pibpib pb '
count = 0
for i in range(len(my_str)):
    if my_str[i] == "0":
        count += 1
        if count == 3:
            print(i + 1)
            break

my_str = '12,34,56'
my_list = my_str.split(',')
print(sum(list(map(int, my_list))))

my_date = '2025-12-31'
date_dict = {}
my_list = my_date.split('-')
my_dict = {'year':my_list[0], 'month':my_list[1], 'day':my_list[2]}

print("{")
for item in my_dict.items():
    print("     '",item[0], "': ", item[1], ",", sep='')
print("}")

my_dict = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
}

list_of_values = set(my_dict.values())
print(list_of_values)

