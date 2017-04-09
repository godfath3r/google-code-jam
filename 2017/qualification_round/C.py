from __builtin__ import xrange
import sys


def left_s(stall, pos):
    rev = stall[:pos]
    rev.reverse()
    return rev.index(1)

def right_s(stall, pos):
    if sum(stall) > 1:
        return stall[pos+1:].index(1)
    else:
        return len(stall) - 1

def print_stall(stall):
    for i in stall:
        if i == 1:
            sys.stdout.write('|')
        if i == 0:
            sys.stdout.write('.')
    print

def get_lrs(stalls):
    lr = []
    for i in xrange(len(stalls)-1, 0, -1):
        if stalls[i] == 0:
            # Left search
            l = left_s(stalls, i)
            # Right search
            r = right_s(stalls, i)
            lr.insert(0, (i - 1, (l, r)))
    return lr


def update_lr(lr, position):
    print lr
    print position
    lrs = [x[0] for x in lr]
    index = lrs.index(position)
    new_lr = []
    _break = False
    for i in xrange(index+1, len(lr)):
        tmp = lr[i]
        if tmp[1][0] > 0 and not _break:
            new_lr.append((tmp[0], (tmp[1][0] - 1,tmp[1][1])))
        else:
            _break = True
            new_lr.append(tmp)
    _lr = lr[:index]
    _lr.reverse()
    _break = False
    for i in xrange(len(_lr)):
        tmp = _lr[i]
        if tmp[1][1] > 0 and not _break:
            new_lr.insert(0, (tmp[0], (tmp[1][0], tmp[1][1]-1)))
        else:
            _break = True
            new_lr.insert(0, tmp)
    return new_lr


def occupy(lr, stalls):
    cord = [x[1] for x in lr]
    mins = [min(x) for x in cord]
    max_min = max(mins)
    if mins.count(max_min) <= 1:
        position = lr[mins.index(max_min)][0]
    else:
        to_add = []
        for i, _min in enumerate(mins):
            if _min == max_min:
                to_add.append(lr[i])
        # print 'to_add->', to_add
        cord1 = [x[1] for x in to_add]
        maxes = [max(x) for x in cord1]
        max_max = max(maxes)
        position = to_add[maxes.index(max_max)][0]
    stalls[position + 1] = 1
    lr = update_lr(lr, position)
    return stalls[:], position, lr

def solve(stalls, ppl):
    lr = get_lrs(stalls)
    for i in xrange(ppl):
        # lr = get_lrs(stalls)
        stalls, pos, lr = occupy(lr, stalls)
        # print_stall(stalls)
    _full = all([x == 1 for x in stalls])
    if _full:
        # print 'FULL'
        return '0 0'
    for x in lr:
        if x[0] == pos:
            return '{} {}'.format(x[1][1], x[1][0])

i = 1
for test in range(int(raw_input().strip())):
    num_stalls, people = map(int, raw_input().strip().split())
    stalls = [0 for x in range(num_stalls)]
    stalls.insert(0, 1)
    stalls.append(1)
    print 'Case #{}: {}'.format(i, solve(stalls, people))
    i += 1