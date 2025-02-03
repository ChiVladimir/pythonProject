my_list = [
"http://www.specialdefects.com/v2/", "походить по песку",

"https://multator.ru/draw/", "рисовать мультики",

"http://mailfuture.ru/write/", "письмо в будущее",

"http://kakoysegodnyadennedeli.ru/", "какой сегодня день недели",

"http://first-ever.ru/", "сайт про всё самое первое",

"http://e.ggtimer.com/", "таймер для ежедневных нужд",

"http://tonematrix.audiotool.com/", "сочинять музыку",

"https://virtualpiano.net/", "играть на синтезаторе",

"http://www.sokra.ru/", "расшифровки"

]

new_list = []
for i in range(len(my_list)):
    if "http://" in my_list[i]:
        new_list.append(my_list[i])
print (new_list)

my_str = 'rgibhbiopwbrgibwrgv0wibvjwpibpibpib pb '

for i in range(len(my_str)):
    if my_str[i] == "0":
        print(i)
        break

new_list = []
for i in range(len(my_list)):
    if "http://" not in my_list[i]:
        new_list.append(my_list[i])
print (new_list)

new_list = []
for i in range(10, 1001):
    if int(str(i)[0]) + int(str(i)[1]) == 5:
        new_list.append(i)
print(new_list)

my_str = 'abcdeabc'
my_list = [ch for ch in my_str]
my_set = set(my_list)
print (''.join(sorted(list(my_set))))
