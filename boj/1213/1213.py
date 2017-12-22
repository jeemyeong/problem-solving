import sys

def S(): return input()

def solve(name):
    alpha_count = {}
    for char in name:
        if char in alpha_count:
            alpha_count[char] += 1
        else:
            alpha_count[char] = 1

    odd_count = [char for char in alpha_count if alpha_count[char] % 2 == 1]
    if len(odd_count) > 1:
        return "I'm Sorry Hansoo"
    ret = ""
    if len(odd_count) == 1:
        ret += odd_count[0]
        alpha_count[odd_count[0]] -= 1
    alphabet = ''.join([chr(ord('A') + i) for i in range(26)])
    reversed_alpha = sorted(alphabet, reverse=True)
    for char in reversed_alpha:
        if char in alpha_count and alpha_count[char] > 0:
            lengthen_char = char * (alpha_count[char]//2)
            ret = lengthen_char + ret + lengthen_char
    return ret

def main():
    name = S()
    print(solve(name))

main()
