# Runtime Error
import sys
# import heapq, collections

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def addTree(tree, word):
    if word == "":
        tree[""] = ""
    elif word[0] in tree and type({}) != type(tree[word[0]]):
        temp = tree[word[0]]
        tree[word[0]] = {}
        addTree(tree[word[0]], temp)
        addTree(tree[word[0]], word[1:])
    elif word[0] in tree:
        addTree(tree[word[0]], word[1:])
    else:
        tree[word[0]] = word[1:]

def findTree(tree, word, isRoot):
    # print(word)
    if word == "" or type({}) != type(tree):
        return 0
    if len(tree) == 1 and not isRoot:
        return findTree(tree[word[0]], word[1:], False)
    return findTree(tree[word[0]], word[1:], False)+1

def solve(n, words):
    ans = 0
    tree = {}
    for word in words:
        addTree(tree, word)
    for word in words:
        ans += findTree(tree, word, True)
        # print(findTree(tree, word, True))
        # break
    # print(tree)
    return round(ans/n, 2)

def main():
    try:
        while True:
        # for _ in range(3):
            n = I()
            words = []
            for _ in range(n):
                words.append(S())
            print(solve(n, words))
            # break
    except ValueError:
        pass

main()
