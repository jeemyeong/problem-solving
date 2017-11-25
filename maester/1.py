def solution(nums):
    nums_set = set(nums)
    return min(len(nums)//2, len(nums_set))

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))