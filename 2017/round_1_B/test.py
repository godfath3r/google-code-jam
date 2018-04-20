from itertools import cycle

x = [1,2,3,4,5]
print x
pool = cycle(x)
one = next(pool)
for i in range(len(x)):
    two = next(pool)
    print one, two
    one = two
