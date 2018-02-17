# Not solved

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

def function(cursor, order):
    if order[0] == "L":
        cursor = cursor["prev"] if cursor["prev"] is not None else cursor
    if order[0] == "D":
        cursor = cursor["next"] if cursor["next"] is not None else cursor
    if order[0] == "B" and cursor["prev"] is not None:
        cursor["val"] = " "
        cursor = cursor["prev"]
    if order[0] == "P":
        cursor = {
            "val": order[2],
            "prev": cursor,
            "next": cursor["next"]
        }
        cursor["prev"]["next"] = cursor
        if cursor["next"] is not None:
            cursor["next"]["prev"] = cursor
    return cursor



def solve(text, orders):
    prev = {
        "val": text[0],
        "prev": None,
        "next": None
    }
    first = prev
    for i in range(1, len(text)):
        cur = {
            "val": text[i],
            "prev": prev,
            "next": None            
        }
        prev["next"] = cur
        prev = cur
    for order in orders:
        cur = function(cur, order)
    res = []
    cur = first
    while cur is not None:
        res.append(cur["val"])
        cur = cur["next"]
    return "".join(res)

def main():
    text = S()
    orders = []
    for _ in range(I()):
        orders.append(S())
    print(solve(text, orders))

main()
