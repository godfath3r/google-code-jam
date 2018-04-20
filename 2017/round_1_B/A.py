def solve(D, horses):
    s_horses = sorted(horses)
    # print s_horses
    times = []
    for h in horses:
        times.append((D - h[0]) / float(h[1]))
    # print times
    max_time = max(times)
    return D / float(max_time)
    print 'max:', max_time
    _dict = []
    for i in range(len(horses) - 1):
        print s_horses[i]
        r_speed = s_horses[i][1] - s_horses[i+1][1]
        # print r_speed
        if r_speed:
            time = (s_horses[i+1][0] - s_horses[i][0]) / float(r_speed)
        else:
            time = 'tttt'
        print 'time', time
        # _dict.append((time, horse))
    # print sorted(_dict, reverse=True)
    return 1

i = 1
for test in range(int(raw_input().strip())):
    D, N = map(int, raw_input().strip().split())
    horses = []
    # print D, N
    for horse in range(N):
        Ki, Si = map(int, raw_input().strip().split())
        horses.append((Ki, Si))
    # pprint(D, N)
    # print horses
    print 'Case #{}: {:0.6f}'.format(i, solve(D, horses))
    i += 1