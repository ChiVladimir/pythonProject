input_str_1 = list(str(input()).split('  '))
floor_numbers = list(str(input()).split('  '))
empl_who_leave = int(input())
num_of_empl = input_str_1[0]
time_of_dep = input_str_1[1]



tariff_price = int(input_str[0])
tariff_size =  int(input_str[1])
cost_of_extra_mb = int(input_str[2])
next_month_traffic = int(input_str[3])
month_cost = int

if next_month_traffic <= tariff_size:
    print(tariff_price)
else: print((next_month_traffic - tariff_size) * cost_of_extra_mb + tariff_price)

