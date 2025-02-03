my_list = [1, -2, 3, -4, 5, -6, 7, 8, 9]
count = 0
for i in range(len(my_list)):
    if my_list[i] < 0:
        count += 1
print (count)

new_list = []
for i in range(len(my_list)):
    if my_list[i] >= 0:
        new_list.append(my_list[i])
print (new_list)

my_str = 'abcdeabc'

new_str = my_str[:-2] + my_str[-1]
print(new_str)

my_list = ['походить по песку', 'https://multator.ru/draw/', 'рисовать мультики .html', 'письмо в будущее .html',
           'какой сегодня день недели', 'сайт про всё самое первое', 'таймер для ежедневных нужд .html', 'сочинять музыку',
           'https://virtualpiano.net/', 'играть на синтезаторе', 'расшифровки .html']

new_list = []
suffix = ".html"
for i in range(len(my_list)):
    if my_list[i].endswith(suffix):
        new_list.append(my_list[i])
print (new_list)

my_list = [1.456, 2.125, 3.32, 4.1, 5.34]
new_list = []
for i in range(len(my_list)):
    new_list.append(round(my_list[i], 1))
print (new_list)

my_dict = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
}
list_of_values = []
for v in my_dict.values():
    list_of_values.append(v)
print(list_of_values)



