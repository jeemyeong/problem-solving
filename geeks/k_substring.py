import sys
read = sys.stdin.readline

def longestSubstringWithKUniqueCharacters(string, k):
    char_set= {}
    left = 0; right = 0
    ret = ""; u = 0; length = len(string)
    while right < length:
        if (not string[right] in char_set) or (char_set[string[right]] == 0):
            u+=1; char_set[string[right]] = 0
        char_set[string[right]] += 1
        right += 1
        while u > k:
            char_set[string[left]] -= 1
            if char_set[string[left]] == 0: u-=1
            left += 1
        if right-left > len(ret):
            ret = string[left:right]
    return ret

def run():
    n = int(read().replace("\n", ""))
    for _ in range(n):
        string= read().replace("\n", "")
        k= int(read().replace("\n", ""))
        print(longestSubstringWithKUniqueCharacters(string, k))

run()