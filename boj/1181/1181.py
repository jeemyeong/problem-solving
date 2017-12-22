import sys

def I(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline()[:-1]

def solve(words):
    words = list(words)
    words.sort()
    words.sort(key=lambda word: len(word))
    return "\n".join(words)

def main():
    N = I()
    words = set()
    for _ in range(N):
        words.add(S())

    print(solve(words))

main()
