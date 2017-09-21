def solve(N, T, number_array):
    for _ in range(T):
        max_difference = 0
        max_difference_pair = None
        for i in range(1, N):
            if abs(number_array[i] - number_array[i-1]) > max_difference:
                max_difference = abs(number_array[i] - number_array[i-1])
                max_difference_pair = (i-1, i)
        
        i = max_difference_pair[1]
        if number_array[i-1] > number_array[i]:
            number_array[i-1] -= 1
        else:
            number_array[i] -= 1
    return number_array

def run():
    import sys
    read = sys.stdin.readline
    N, T = map(int, read().split(' '))
    number_array = list(map(int, read().split(' ')))
    new_number_array = solve(N, T, number_array)
    print(" ".join(list(map(str,new_number_array))))

run()
