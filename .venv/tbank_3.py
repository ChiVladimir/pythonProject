num_of_empl, time_of_depart  = map(int, input().split('  '))
floor_numbers = [int(n) for n in input().split('  ')]
empl_who_leave = int(input())


#print(floor_numbers, empl_who_leave, num_of_empl, time_of_depart)

if floor_numbers[-1] - floor_numbers[empl_who_leave-1] <= time_of_depart:
    print(floor_numbers[-1] - floor_numbers[0])

elif floor_numbers[empl_who_leave-1] - floor_numbers[0] <= time_of_depart:
    print(floor_numbers[-1] - floor_numbers[0])

else:
    res1 = (floor_numbers[empl_who_leave-1] - floor_numbers[0]) + (floor_numbers[-1] - floor_numbers[0])
    res2 = (floor_numbers[-1] - floor_numbers[empl_who_leave-1]) + (floor_numbers[-1] - floor_numbers[0])
    print(min([res1, res2]))