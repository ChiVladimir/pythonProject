import sys

def print_seats(seats, n):
    for i in range(n):
        print(seats[i])

def add_pass(row):
    flag = False
    for i in range (6):
        if row[i] == "." and row[5 - i] == "X" and flag == False:
#            print (row[i], row[5 - i])
            li = list(row)
            li[i] = "X"
            row = ''.join(li)
            flag = True
#            print ("ряд", row)
    return row, flag

def free_busy(row):
    return row.count('X'), row.count('.')

def check_balance(row):
    if row[0] == row[5] and row[1] == row[4] and row[2] == row[3]:
        return True
    else:
        return False

inp_str_1 = list(map(int, input().split()))

n = inp_str_1[0] # количество рядов в самолете
m = inp_str_1[1] # количество пассажиров, которые придут на стойку регистрации
seats = []
free_place = 0
busy_place = 0
for i in range(n):
    row = str(input())
    busy_place += free_busy(row)[0]
    free_place += free_busy(row)[1]
    seats.append(row)
#    print (busy_place, free_place)
#print("seats", seats)
#print (busy_place, free_place)
if m == 0: # нет пассажиров без регистрации
    flag = 0
    for i in range (n):
        if check_balance(seats[i]) == False:
            flag = 1
    if flag == 1:
        print('Impossible')
    else:
        print_seats(seats, n)
    sys.exit()
elif free_place < m or (busy_place + m)%2 == 1: # пассажиров пришло больше или пассажиров суммарно нечетное кол-во
#    print("free_place", free_place)
#    print("busy_place + m", busy_place + m)

    print ('Impossible')
    sys.exit()

elif m != 0:
    i = 0
    while i < m:
#        step = str(input())
#        print (i)
#        print ((seats[i]))
#        print("Passengers to board all - ", m)

        for i in range(n):
            x, y = free_busy(seats[i])
#            print(x, y)
            if free_busy(seats[i])[1] == 6 and m >= 2:
                li = list(seats[i])
                li[i] = "X"
                seats[i] = ''.join(li)
                m -= 1
#                print ("leave passengers after sitting into empty row - ", m)
            for j in range(m):
#                print("Passengers to board leave for sitting - ", m)
                new_row, flag = add_pass(seats[i])
#                print("сажаем ", new_row, flag)
                seats[i] = new_row
#                print (seats[i])
                if flag == False:
                    break
                else:
                    m -= 1
#            print(n)
    print_seats(seats, n)