def solve(_list):
    length = len(_list)
    step = 3
    done = False
    while not done:
        done = True
        # print _list
        for i in range(0, length-2):
            # print _list[i:step]
            if _list[i] > _list[i+2]:
                done = False
                x = _list[i]
                _list[i] = _list[i+2]
                _list[i+2] = x
        # print _list
    sorted_list = sorted(_list)
    if _list == sorted_list:
        return 'OK'
    else:
        # print '---->', sorted_list
        for i in range(length):
            if sorted_list[i] != _list[i]:
                return str(i)

i = 1
for test in range(int(raw_input().strip())):
    raw_input().strip().split()
    list_ = map(int, raw_input().strip().split())
    print 'Case #{}: {}'.format(i, solve(list_))
    i += 1