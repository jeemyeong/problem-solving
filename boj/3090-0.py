def get_max_difference_pair(N, number_array):
    max_difference = 0
    max_difference_pairs = []
    for i in range(1, N):
        if abs(number_array[i] - number_array[i-1]) > max_difference:
            max_difference = abs(number_array[i] - number_array[i-1])
            max_difference_pairs = [(i-1, i)]
        if abs(number_array[i] - number_array[i-1]) == max_difference:
            max_difference_pairs.append((i-1, i))
    return max_difference, max_difference_pairs

def solve(N, T, number_array):
    from collections import deque
    q = deque([])
    q.append((T, [n for n in number_array]))
    number_array_to_return = [n for n in number_array]
    max_difference_to_return = 1e100
    while q:
        T, number_array = q.popleft()
        max_difference, max_difference_pairs = get_max_difference_pair(N, number_array)
        if max_difference_to_return > max_difference:
            max_difference_to_return = max_difference
            number_array_to_return = number_array

        if T <= 0 or max_difference == 0:
            continue
        for max_difference_pair in max_difference_pairs:
            i = max_difference_pair[1]
            signal = 1 if number_array[i] > number_array[i-1] else 2

            new_number_array1 = [n for n in number_array]
            new_number_array1[i-1] += signal
            q.append((T-1, new_number_array1))

            new_number_array2 = [n for n in number_array]
            new_number_array2[i] -= signal
            q.append((T-1, new_number_array2))
    return [n for n in number_array_to_return]

def run():
    import sys
    read = sys.stdin.readline
    N, T = map(int, read().split(' '))
    number_array = list(map(int, read().split(' ')))
    new_number_array = solve(N, T, number_array)
    print(" ".join(list(map(str, new_number_array))))

run()
