from sympy import *

def create_symbols(n):
    return symbols("n{0} Q{0} lx{0} ly{0} g{0}".format(n))

def link(ba, bb, lx, ly, g):
    n0, Q0, lx0, ly0, g0 = ba
    n1, Q1, lx1, ly1, g1 = bb

    return [-n0 + lx0 + n1, -Q0 + ly0 + g0 + Q1, lx0-lx, ly0-ly, g0-g]

def end(ba):
    n0, Q0, lx0, ly0, g0 = ba
    return [n0,Q0,lx0,ly0,g0]

b0 = create_symbols(0)
b1 = create_symbols(1)
b2 = create_symbols(2)

l1 = link(b0, b1, 0, 1, 0)
l2 = link(b1, b2, 0, 1, 0)
e = end(b2)

print(linsolve(l1+l2+e, b0 + b1 + b2))
