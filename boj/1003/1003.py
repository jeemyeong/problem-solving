dp = {0: (1, 0), 1: (0, 1)}

def fibonacci(n):
    if n not in dp:
        left = fibonacci(n-1)
        right = fibonacci(n-2)
        
        dp[n] = (left[0]+right[0], left[1]+right[1])
    return dp[n]

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        x, y = fibonacci(N)
        print(x, y)

