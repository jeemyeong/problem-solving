import sys
# Not solved
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def match(j, history, lst):
    if lst[j] in history and history[lst[j]] != None:
        lst[history[lst[j]]] = None
        lst[j] *= 2

        match(j, history, lst)
        

def solve(n, lst):
    history = dict()
    length = len(lst)

    for i in range(length):
        matched = False
        for j in range(i+1, length):
            if lst[i] == lst[j]:
                matched = True
                lst[i] = None
                lst[j] *= 2
                match(j, history, lst)
                break
        if not matched:
            history[lst[i]] = i
    cnt = 0
    for i in lst:
        if i != None:
            cnt+=1
    print(cnt)

    for i in list(filter(lambda x: x!= None, lst)):
        print(i, end=" ")

def main():
    n = I()
    lst = LI()
    solve(n, lst)

main()
