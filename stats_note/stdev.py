"""
Sample Input

5
10 40 30 50 20
Sample Output

14.1
"""

n = input()
x = input()

#n = '10'
#x = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'

n = int(n)
x = x.split()

mu = sum(map(lambda i: int(i), x)) / n
x = map(lambda i: (int(i)-mu)**2, x)

#print(mu, n)

print("%0.1f" % ((sum(x)/n)**0.5))
