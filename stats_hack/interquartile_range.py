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

    return first_half, second_half, median

n = input()
elements = input()
frequency = input()

n = 6
elements = '6 12 8 10 20 16'
frequency = '5 4 3 2 1 5'

elements = list(map(int, elements.split(' ')))
frequency = list(map(int, frequency.split(' ')))

elements_frequency_dict = {}
for index, item in enumerate(elements):
    elements_frequency_dict[item] = frequency[index]

elements_frequency_dict = sorted(elements_frequency_dict.items())
inp_sorted = []
for item, count in elements_frequency_dict:
    for i in range(count):
        inp_sorted.append(item)


first_half, second_half, q2 = get_quartile(inp_sorted)
_, _, q1 = get_quartile(first_half)
_, _, q3 = get_quartile(second_half)

print("%.1f" % (q3 - q1))
