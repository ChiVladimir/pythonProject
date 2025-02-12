input_str = str(input()).split()

tariff_price = int(input_str[0])
tariff_size =  int(input_str[1])
cost_of_extra_mb = int(input_str[2])
next_month_traffic = int(input_str[3])
month_cost = int

if next_month_traffic <= tariff_size:
    print(tariff_price)
else: print((next_month_traffic - tariff_size) * cost_of_extra_mb + tariff_price)

