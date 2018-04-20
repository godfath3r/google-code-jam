from itertools import cycle

def can_mix(u1, u2):
    mix = {'R': 'R', 'O': 'RY', 'Y': 'Y', 'G': 'YB', 'B': 'B',
           'V': 'BR'}
    t = [False if x in mix[u2] else True for x in mix[u1]]
    return all(t)

def fit_in_stals(N, stals, unicorn):
    if len(stals) == 1:
        if can_mix(stals[0], unicorn):
            stals.append(unicorn)
            # print stals
            return True, stals
    else:
        pool = cycle(stals)
        pos = 1
        one = next(pool)
        for i in range(len(stals)):
            two = next(pool)
            # print 'can_mix:', one, unicorn, two, [can_mix(one, unicorn), can_mix(two, unicorn)]
            # print 'pos', pos
            if can_mix(one, unicorn) and can_mix(two, unicorn):
                stals.insert(pos, unicorn)
                print 'append', unicorn, 'one, two', one, two, stals
                return True, stals
            pos += 1
            one = two
    return False, stals


def solve(N, unicorn):
    # print N, unicorn

    unis = []
    _map = ['R', 'O', 'Y', 'G', 'B', 'V']
    for i, u in enumerate(unicorn):
        if u:
            for k in xrange(unicorn[i]):
                unis.append(_map[i])
    print unis

    stals = [unis[0]]
    del unis[0]
    not_even_one = 0
    while unis:
        # print 'Unis:', unis
        not_even_one = 0
        if not len(unis):
            return stals
        if not_even_one >= len(unis) - 1:
            return 'IMPOSSIBLE'
        print stals, not_even_one, len(unis)
        for i in xrange(len(unis)):
            # print unis
            done, stals = fit_in_stals(N, stals, unis[i])
            if done:
                del unis[i]
                break
            else:
                not_even_one += 1
    return stals


i = 1
for test in range(int(raw_input().strip())):
    N, R, O, Y, G, B, V = map(int, raw_input().strip().split())
    unicorn = (R, O, Y, G, B, V)
    # pprint(D, N)
    # print horses
    print 'Case #{}: {}'.format(i, solve(N, unicorn))
    i += 1