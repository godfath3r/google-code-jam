def get_damage(sequence):
    dmg = 1
    dmg_done = 0
    for action in sequence:
        if action == 'S':
            dmg_done += dmg
        if action == 'C':
            dmg = dmg * 2
    # print 'Damage:', dmg_done
    return dmg_done

def there_is_change(sequence):
    seq = ''.join(sequence)
    s = seq.rfind('S')
    return 'C' in seq[:s]

def do_(D, seq):
    changes = 0
    # print 'Length:', length
    # print sequence
    sequence = [x for x in seq]
    length = len(sequence)
    while there_is_change(sequence):
        # print sequence
        for i in range(length, 1, -1):
            # print i
            if sequence[i-1] == 'S' and sequence[i-2] == 'C':
                sequence[i-1] = "C"
                sequence[i-2] = "S"
                changes += 1
                if get_damage(sequence) <= D:
                    return changes
        # print sequence
    return "IMPOSSIBLE"


def solve(D, P):
    # print 'D:', D, 'P:', P
    nums = P.count('S')
    numc = P.count('C')
    min = 2 ^ P.count('C')

    if 'S' not in P:
        return '0'
    if nums > D:
        return 'IMPOSSIBLE'
    damage = get_damage(P)
    if damage <= D:
        return "0"
    else:
        return do_(D, P)


i = 1
for test in range(int(raw_input().strip())):
    D, P = raw_input().strip().split()
    D = int(D)
    P = str(P)
    print 'Case #{}: {}'.format(i, solve(D, P))
    i += 1