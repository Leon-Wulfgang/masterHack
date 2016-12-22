"""
Sample Input
9
3 7 8 5 12 14 21 13 18

Sample Output
6
12
16
"""


def get_quartile(arr_int_sorted):

    count = len(arr_int_sorted)

    # even
    if 0 == count % 2:
        median = (arr_int_sorted[int(count/2 - 1)] + arr_int_sorted[int(count/2)]) / 2
        first_half = arr_int_sorted[:int(count/2)]
        second_half = arr_int_sorted[int(count/2):]

    # odd
    else:
        median = arr_int_sorted[int(count/2)]
        first_half = arr_int_sorted[:int(count / 2)]
        second_half = arr_int_sorted[int(count / 2 + 1):]

    return first_half, second_half, int(median)

n = input()
inp = input()
inp = '3 7 8 5 12 14 21 13 18'

inp = list(map(int, inp.split(' ')))
inp_sorted = sorted(inp)

first_half, second_half, q2 = get_quartile(inp_sorted)
_, _, q1 = get_quartile(first_half)
_, _, q3 = get_quartile(second_half)

print(q1, q2, q3, sep='\n')
