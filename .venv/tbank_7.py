import copy

def gift_distrib(bad_santa):
    rpt_index = []
    miss_index = []
    result = [-1, -1]

    bad = set(bad_santa)
    ch = sum(bad_santa) - sum(bad)
    for number in range(1, len(bad_santa) + 1):
        if number not in bad:
            miss_index.append(number)
        elif number == ch:
            duplicate = []
            for c, l in enumerate(bad_santa):
                if l == number:
                    duplicate.append(c)
            if len(duplicate) == 2:
                rpt_index.append(duplicate[0])
                rpt_index.append(duplicate[1])

    for i in rpt_index:
        for j in miss_index:
            back = [bad_santa[i]]
            bad_santa[i] = int(j)
            cycle_count_rpt_index = 0
            copy_2 = copy.deepcopy(bad_santa)
            lost_idx = bad_santa[0]

            while len(bad_santa) > cycle_count_rpt_index:
                copy_2[lost_idx - 1] *= -1
                lost_idx = bad_santa[lost_idx - 1]
                cycle_count_rpt_index += 1
            second_cycle_count = 0

            for marker in copy_2:
                if marker < 0:
                    second_cycle_count += 1
            if second_cycle_count == len(bad_santa) or sum(copy_2) == -sum(bad_santa):
                result = [i + 1, j]
                break
            else:
                bad_santa[i] = back[0]
                continue

    return result



len_bad_santa = int(input())
bad_santa = [int(n) for n in input().split()]
res = gift_distrib(bad_santa)
print(res[0], res[1])
