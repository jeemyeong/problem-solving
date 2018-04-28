def move_left(bits, n):
    return bits << n

def has_number(bits, n):
    return (bits >> n) % 2 == 1

def solve(input_list):
    bits = 0
    for num in input_list:
        if has_number(bits, num):
            bits -= move_left(1, num)
        else:
            bits += move_left(1, num)
    ret = []
    cnt = 0
    while len(ret) < 2:
        if (bits % 2 == 1):
            ret.append(cnt)
        cnt += 1
        bits //= 2
    return ret

print(solve([2, 1, 5, 6, 6, 1]))
print(solve([9, 9, 4, 3]))
