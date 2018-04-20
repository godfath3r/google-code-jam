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

lr = [(0, (0, 4)), (1, (1, 3)), (2, (2, 2)), (3, (3, 1)), (4, (4, 0)), (6, (0, 1)), (7, (1, 0))]
lr = [(0, (0, 3)), (1, (1, 2)), (3, (2, 1)), (4, (3, 0))]
print update_lr(lr, 1)