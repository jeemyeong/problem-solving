import sys

def I(): return int(sys.stdin.readline())
def S(): return input()

class Trie(object):
    def __init__(self, initial = False):
        if initial:
            self.trie = {"initial": True}
        else:
            self.trie = {"initial": False}
    
    def insert(self, node):
        if len(node) == 0:
            return
        if node[0] in self.trie:
            self.trie[node[0]].insert(node[1:])
        else:
            self.trie[node[0]] = Trie()
            self.trie[node[0]].insert(node[1:])
    
    def count(self):
        return len(self.trie)-1

    def isInitial(self):
        return self.trie["initial"]

    def isEmpty(self):
        if self.count() == 0:
            return True
        else:
            return False

    def check(self, node):
        if len(node) == 0 or (self.isEmpty() and not self.isInitial()):
            return True
        if node[0] in self.trie:
            return self.trie[node[0]].check(node[1:])
        else:
            return False

def solve2(lst): #51588 KB 7644 MS
    trie = Trie(initial = True)
    for item in lst:
        if trie.check(item):
            return "NO"
        trie.insert(item)
    return "YES"


def insertToTrie(trie, node):
    if len(node) == 0:
        return
    if node[0] in trie:
        insertToTrie(trie[node[0]], node[1:])
    else:
        trie[node[0]] = {}
        insertToTrie(trie[node[0]], node[1:])

def checkInTrie(trie, node):
    if len(node) == 0 or len(trie) == 0:
        return True
    if node[0] in trie:
        return checkInTrie(trie[node[0]], node[1:])
    else:
        return False

def solve3(lst): #41924 KB 6420 MS
    trie = {"INITIAL": "TRUE"}
    for item in lst:
        if checkInTrie(trie, item):
            return "NO"
        insertToTrie(trie, item)
    return "YES"

def solve(lst): #29128 KB 5392 MS
    lst.sort()
    for i in range(len(lst)-1):
        if len(lst[i]) < len(lst[i+1]) and lst[i] == lst[i+1][:len(lst[i])]:
            return "NO"

    return "YES"

def main():
    t = I()
    for _ in range(t):
        n = I()
        lst = []
        for _ in range(n):
            lst.append(S())
        print(solve(lst))

main()
