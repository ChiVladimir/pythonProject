import heapq

qnt_of_nums, iter_lim = map(int, input().split()) # n, k — количество чисел на бумажке и ограничение на число операций.
numbers = [int(n) for n in input().split()]
chng_list = []
incr_amnt = 0

base_sum = sum(numbers)

calc_list = sorted(numbers, reverse=True)

#print (calc_list, len(calc_list))


for i in range(len(calc_list)):
    for j in range(len(str(calc_list[i]))):
#            print ("i-", i, "j-", j, "len", len(str(calc_list[i])), 9 - int(str(calc_list[i])[j]))
#            print(10 ** (len(str(calc_list[i]))-j-1))
            chng_dgt = (10 ** (len(str(calc_list[i]))-j-1)) * (9 - int(str(calc_list[i])[j]))
#            print("--------chng_dgt", chng_dgt)
            chng_list.append(chng_dgt)
    # except IndexError:
    #     pass

res = heapq.nlargest(iter_lim, chng_list)
# print ("chng_list -", chng_list)
# print ("res -", res)

try:
    for k in range(iter_lim):
        incr_amnt += res[k]
except IndexError:
    pass

print(incr_amnt)

