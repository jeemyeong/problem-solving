import sys
read = sys.stdin.readline

def longestSubstringWithKUniqueCharacters(string, k):
    ret = ""
    ret_size = 0
    n = len(string)
    _hash = {}
    unique = 0
    lastIdx = 0
    for i in range(n):
        new = string[i]
        if (new not in _hash) or (new in _hash and _hash[new]==0):
            _hash[new] = 1
            unique += 1
        else:
            _hash[new] += 1
        while unique > k:
            last = string[lastIdx]
            if _hash[last] > 1:
                lastIdx += 1
                _hash[last] -= 1
            else:
                lastIdx += 1
                _hash[last] = 0
                unique -= 1
        if unique == k and i+1-lastIdx > ret_size:
            ret = string[lastIdx:i+1]
            ret_size = i+1-lastIdx
    if ret != "":
        return ret_size
    else:
        return -1

def run():
    n = int(read().replace("\n", ""))
    for _ in range(n):
        string= read().replace("\n", "")
        k= int(read().replace("\n", ""))
        print(longestSubstringWithKUniqueCharacters(string, k))

run()