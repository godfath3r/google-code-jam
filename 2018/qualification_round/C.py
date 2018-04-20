import sys
pos = [5, 7, 9]

def _print(x):
    print x
    sys.stdout.flush()

def _print_(x):
    sys.stderr.write(x+'\n')
    sys.stderr.flush()

def is_full(c, coordinates, tries):
    nin = [(c[0] - 1, 4), (c[0], 4), (c[0] + 1, 4),
           (c[0] - 1, 5), (c[0], 5), (c[0] + 1, 5),
           (c[0] - 1, 6), (c[0], 6), (c[0] + 1, 6)]
    y = all(x in coordinates for x in nin)
    # if y:
        # _print_("Coordinates: {}".format(sorted(coordinates)))
        # _print_("TRUEEE {} {}".format(c[0], tries))
    return y

def decide_position(tries, coords):
    # _print_("COORDS {} {}".format(coords, tries))
    global pos
    mod = tries % len(pos)
    c = (pos[mod], 5)
    if is_full(c, coords, tries):
        pos.remove(pos[mod])
    return '{} {}'.format(c[0], c[1])

def is_valid(coord):
    if coord[0] == -1 and coord[1] == -1:
        return False
    return True

def init_pos(A):
    global pos
    if A == 20:
        pos = [5, 7, 9]
    if A == 200:
        pos = [x for x in range(5, 70, 2)]
    # _print_('POSO: {}'.format(pos))

def solve(tries, A):
    coordinates = []
    # x, y = map(int, raw_input().strip().split())
    init_pos(A)
    done = False
    while not done:
        _print(decide_position(tries, coordinates))
        x, y = map(int, raw_input().strip().split())
        tries += 1

        if x == 0 and y == 0:
            # _print_("Found it!")
            done = True
        if is_valid((x, y)):
            if (x, y) not in coordinates:
                coordinates.append((x, y))
        else:
            pass
            # _print_("Invalid")
            # done = True
        # _print_("xy: {} {}".format(x, y))
    return tries


i = 1
tests = int(raw_input().strip())
statistics = []
for test in range(tests):
    # _print_("tests {}".format(tests))
    A = int(raw_input().strip())
    # _print_("A is {}".format(A))
    TRIES = 0
    statistics.append(solve(TRIES, A))
    i += 1
_print_("Max tries {}".format(max(statistics)))
_print_("Min tries {}".format(min(statistics)))