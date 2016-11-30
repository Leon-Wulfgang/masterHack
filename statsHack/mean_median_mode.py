"""
Given an array, , of  integers, calculate and print the the respective mean, median, and mode on separate lines.
If your array contains more than one modal value, choose the numerically smallest one.
Note: Other than the modal value (which will always be an integer), your answers should be in decimal form,
rounded to a scale of  decimal place (i.e., ,  format).
"""


def mean(x):
    return float(sum(x))/(len(x))


def median(x):
    x = list(x)
    x.sort()
    middle_point_int = len(x) // 2
    #print(middle_point_int)
    if(len(x) % 2) == 0:
        return (x[middle_point_int-1]+x[middle_point_int])/2.0
    else:
        return x[middle_point_int-1]


def mode(x):
    d = {}
    for element in x:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    sorted_d = sorted(d.items(), key=lambda a: a[1], reverse=True)
    max_occ = sorted_d[0][1]
    min_num = sorted_d[0][0]
    for num, occ in sorted_d:
        if occ < max_occ:
            break
        min_num = min(min_num, num)
    #print(sorted_d, max_occ, min_num)
    return min_num

n = input()
inp = input()
#inp = "4 4 3 2 1 1"
#inp = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
inp = list(map(int, inp.split(' ')))

mean = mean(inp)
median = median(inp)
mode = mode(inp)

#print(inp)

print(mean)
print(median)
print(mode)
