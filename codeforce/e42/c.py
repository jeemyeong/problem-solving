import sys
import math

def I(): return int(sys.stdin.readline())

def is_square(n):
    i = int(math.sqrt(n)) #sqrt function returns float so typecasting to int
    if n == i*i:
        return True
    else:
        return False

def solve(n):
    _set = {n}
    cnt = 0
    while len(_set) > 0:
        _new_set = set()
        for _ in range(len(_set)):
            i = _set.pop()
            if is_square(i):
                return cnt
            splitInt = list(str(i))

            if len(splitInt) == 1:
                continue
            for j in range(len(splitInt)):
                if j == 0 and splitInt[1] == '0':
                    continue
                _new_set.add(int("".join(splitInt[:j] + splitInt[j+1:])))
        _set = _new_set
        _new_set = set()
        cnt += 1
    return -1

def main():
    print(solve(I()))

main()
