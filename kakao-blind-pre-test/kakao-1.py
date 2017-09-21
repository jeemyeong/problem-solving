def solution(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

print(solution(123))
