from __builtin__ import xrange

def is_tidy(number):
    list = [x for x in str(number)]
    s_list = sorted(list)
    # print list, s_list
    if list == s_list:
        return True
    return False

def find_next(number):
    # print number
    list = [int(x) for x in str(number)]
    first = list[0]
    for i in xrange(1, len(list)):
        if first > list[i]:
            for k in range(len(list[i:])):
                list[i+k] = 0
            new_num = int(''.join(map(str, list)))
            return new_num - 1
        first = list[i]

def solve(num):
    while not is_tidy(num):
        num = find_next(num)
    return num

i = 1
for test in range(int(raw_input().strip())):
    num = int(raw_input().strip())
    print 'Case #{}: {}'.format(i, solve(num))
    i += 1