import sys

def main():
    n = int(sys.stdin.readline())
    nums = [0 for x in range(10001)]
    for _ in range(n):
        nums[int(sys.stdin.readline())] += 1
    for i in range(10001):
        if nums[i] > 0:
            print((str(i)+"\n") * nums[i], end="")
main()
