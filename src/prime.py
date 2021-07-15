import math

def pc(m):
    a = [1] * m
    a[:2] = [0, 0]
    for p in range(m):
        if a[p]:
            a[2 * p: m: p] = [0] * math.ceil(m / p - 2)
    return sum(a)

assert pc(    10_000) ==   1_229
assert pc(   100_000) ==   9_592
assert pc( 1_000_000) ==  78_498
# assert pc(10_000_000) == 664_579


if __name__ == '__main__':
    for i in [10, 100, 1_000, 10_000]:
        print(i, pc(i))