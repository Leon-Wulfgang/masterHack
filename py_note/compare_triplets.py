#!/bin/python

import sys

ai = "5 6 7"
bi = "3 6 10"

a0,a1,a2 = ai.strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = bi.strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

aa = [a0, a1, a2]
bb = [b0, b1, b2]
ac, bc = 0, 0

for i in range(0, len(aa)):
    ac += int(aa[i] > bb[i])
    bc += int(aa[i] < bb[i])

#print aa,bb
print ac,bc
