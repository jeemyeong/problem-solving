def solution(arr):
    _set = set(arr)
    return len(_set) == len(arr) and len(arr) == max(_set)

print(solution([4, 1, 3]))
