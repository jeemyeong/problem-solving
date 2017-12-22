import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def solve(N, H, from_down, from_up):
    each_obstacle_by_position = [0 for _ in range(H)]

    each_obstacle_by_position[H-2] += from_down[H-2]
    for i in range(H-3, -1, -1):
        from_down[i] += from_down[i+1]
        each_obstacle_by_position[i] += from_down[i]

    each_obstacle_by_position[1] += from_up[0]
    for i in range(1, H-1):
        from_up[i] += from_up[i-1]
        each_obstacle_by_position[i+1] += from_up[i]

    min_obstacle_by_position = min(each_obstacle_by_position)
    min_obstacle_count = len([x for x in each_obstacle_by_position
                              if x == min_obstacle_by_position])

    return "%s %s" % (min_obstacle_by_position, min_obstacle_count)

def main():
    N, H = LI()
    from_down = [0 for _ in range(H-1)]
    from_up = [0 for _ in range(H-1)]
    for _ in range(N//2):
        from_down[I() - 1] += 1
        from_up[H - I() - 1] += 1
    print(solve(N, H, from_down, from_up))

main()
