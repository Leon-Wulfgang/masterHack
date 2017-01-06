"""
Given an array, , of  integers and an array, , representing the respective weights of 's elements,
calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of
decimal place (i.e.,  format).
"""

'''
n = input()
x = input()
w = input()
'''

n = 10
x = '10 40 30 50 20 10 40 30 50 20'
w = '1 2 3 4 5 6 7 8 9 10'

n = int(n)
x = list(map(int, x.split(' ')))
w = list(map(int, w.split(' ')))

print(x, w)

g = lambda j, k: j * k

t = 0
for i in range(0, n):
    t += g(x[i], w[i])

result = "%.1f" % round(t/sum(w), 1)

print(result)
