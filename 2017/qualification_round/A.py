def is_solved(cake):
    if all([x == '+' for x in cake]):
        return True, False
    if all([x == '-' for x in cake]):
        return True, True
    return False, False


def flip_cake(cake, pos, S):
    cake = [c for c in cake]
    for i in range(S):
        if cake[pos + i] == '+':
            cake[pos + i] = '-'
        else:
            cake[pos + i] = '+'
    return ''.join(cake)

def solve(cake, S):
    # print cake, S
    length = len(cake)
    if all([x == '+' for x in cake]):
        return 0
    if S > length:
        return 'IMPOSSIBLE'
    if all([x == '-' for x in cake]):
        if S == length:
            return 1
        if length % S == 0:
            return length / S
        else:
            return 'IMPOSSIBLE'
    flips = 0
    for i in range(length - S + 1):
        # print cake
        portion = cake[i:i+S]
        # print 'Portion: ', portion
        if portion.startswith('-'):
            cake = flip_cake(cake, i, S)
            flips += 1
    is_solv, one_more = is_solved(cake)
    if is_solv:
        if one_more:
            return flips + 1
        return flips
    else:
        return 'IMPOSSIBLE'


i = 1
for test in range(int(raw_input().strip())):
    cakes, S = raw_input().strip().split()
    print 'Case #{}: {}'.format(i, solve(cakes, int(S)))
    i += 1