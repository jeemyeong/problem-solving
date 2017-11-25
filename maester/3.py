def solution(arr): #O(n^3)
    return get_max(arr, 0, len(arr)-1, {}, {})

def get_min(arr, a, b, dp_min, dp_max):
    if (a, b) in dp_min:
        return dp_min[(a, b)]
    if a == b:
        dp_min[(a, b)] = int(arr[a])
        return dp_min[(a, b)]
    min_list = []
    for i in range(a+1, b, 2):
        operator = arr[i]
        if operator == "+":
            item = get_min(arr, a, i-1, dp_min, dp_max) + get_min(arr, i+1, b, dp_min, dp_max)
            min_list.append(item)
        if operator == "-":
            item = get_min(arr, a, i-1, dp_min, dp_max) - get_max(arr, i+1, b, dp_min, dp_max)
            min_list.append(item)
    return min(min_list)

def get_max(arr, a, b, dp_min, dp_max):
    if (a, b) in dp_min:
        return dp_min[(a, b)]
    if a == b:
        dp_min[(a, b)] = int(arr[a])
        return dp_min[(a, b)]
    max_list = []
    for i in range(a+1, b, 2):
        operator = arr[i]
        if operator == "+":
            item = get_max(arr, a, i-1, dp_min, dp_max) + get_max(arr, i+1, b, dp_min, dp_max)
            max_list.append(item)
        if operator == "-":
            item = get_max(arr, a, i-1, dp_min, dp_max) - get_min(arr, i+1, b, dp_min, dp_max)
            max_list.append(item)
    return max(max_list)

def solution2(arr): #O(n!)
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
        if random.randint(1, 4) == 1:
            arr.append("+")
        else:
            arr.append("-")
    arr.pop()
    return arr

# print(solution(['1', '-', '4', '+', '5', '-', '1', '-', '2', '-', '3', '+', '2', '-', '3']))
# print(solution2(['1', '-', '4', '+', '5', '-', '1', '-', '2', '-', '3', '+', '2', '-', '3']))
