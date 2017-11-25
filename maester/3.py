# Not solved

# def solution(arr):
#     n = len(arr)//2+1
#     dp = [{"max": None, "min": None} for _ in range(n+1)]
#     dp[n] = {"max": 0, "min": 0}
#     for i in range(n-1, -1, -1):
#         operator = arr[2*i-1]
#         operand = int(arr[2*i])
#         if operator == "-":
#             nums = [-operand+dp[i+1]["max"], -operand-dp[i+1]["max"], -operand+dp[i+1]["min"], -operand-dp[i+1]["min"]]
#             dp[i]["max"] = max(nums)
#             dp[i]["min"] = min(nums)
#         else:
#             nums = [operand+dp[i+1]["max"], operand+dp[i+1]["min"]]
#             dp[i]["max"] = max(nums)
#             dp[i]["min"] = min(nums)
#     return dp[0]["max"]

# print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))

def solution1(arr):
    n = len(arr)//2+1
    dp = [set([]) for _ in range(n+1)]
    dp[n] = set([0])
    for i in range(n-1, -1, -1):
        operator = arr[2*i-1]
        operand = int(arr[2*i])
        if i > 0 and operator == "-":
            for num in dp[i+1]:
                dp[i].add(-operand+num)
                dp[i].add(-operand-num)
        else:
            for num in dp[i+1]:
                dp[i].add(operand+num)
    return max(dp[0])

def solution(arr):
    n = len(arr)//2+1
    new_arr = [int(arr[0])]
    for i in range(n-1):
        operator = arr[2*i+1]
        operand = int(arr[2*i+2])
        if operator == "+":
            new_arr[-1] += operand
        else:
            new_arr.append("-")
            new_arr.append(operand)
    return max(solution1(new_arr), solution1(arr))

def solution2(arr):
    n = len(arr)//2+1
    if n == 1:
        return int(arr[0])
    ans = []
    for i in range(n-1):
        operator = arr[2*i+1]
        operand = (int(arr[2*i]), int(arr[2*i+2]))
        if operator == "+":
            new_arr = arr[:2*i] + [str(operand[0] + operand[1])] + arr[2*i+3:]
            ans.append(solution2(new_arr))
        else:
            new_arr = arr[:2*i] + [str(operand[0] - operand[1])] + arr[2*i+3:]
            ans.append(solution2(new_arr))
    return max(ans)


def random_arr():
    import random

    n = random.randint(4, 5)
    arr = []
    for _ in range(n):
        arr.append(str(random.randint(1, 5)))
        if random.randint(1,4) == 1:
            arr.append("+")
        else:
            arr.append("-")
    arr.pop()
    return arr

# # for _ in range(100000):
#     arr = random_arr()
#     sol1 = (solution(arr))
#     sol2 = (solution2(arr))
#     if sol1 != sol2:
#         print(arr)
#         print(sol1)
#         print(sol2)
#         break

print(solution(['1', '-', '4', '+', '5', '-', '1', '-', '2', '-', '3', '+', '2', '-', '3']))
print(solution2(['1', '-', '4', '+', '5', '-', '1', '-', '2', '-', '3', '+', '2', '-', '3']))