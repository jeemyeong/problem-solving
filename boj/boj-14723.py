def solve(n):
    i = 1
    while (i*(i+1)/2) < n:
        i+=1
    i-=1
    j = n - int(i*(i+1)/2)
    i -= j - 2
    return (i, j)

def run():
    n = int(input())
    print(" ".join(list(map(str, solve(n)))))

run()
