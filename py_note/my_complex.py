

# custom complex class with custom string format function
class MyComplex(complex):
    def __str__(self):
        return '{0:.2f}{1:+.2f}i'.format(self.real, self.imag)

# inputs
inp = [
    "2 1",
    "5 6"
]

# trim input
a, b = map(float, inp[0].split()), map(float, inp[1].split())

# init complex numbers
c, d = complex(a[0], a[1]), complex(b[0], b[1])

# do math
addition = MyComplex(c+d)
subtraction = MyComplex(c-d)
multiplication = MyComplex(c*d)
division = MyComplex(c/d)
modulus_c = MyComplex(abs(c))
modulus_d = MyComplex(abs(d))

# output formatted complex numbers
print '\n'.join(map(str,[addition, subtraction, multiplication, division, modulus_c, modulus_d]))



