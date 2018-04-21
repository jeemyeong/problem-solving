def solve(string):
    stack = [[1, ""]]
    i = 0
    length = len(string)
    num = ""
    while i < length:
        cur = string[i]
        i+=1
        if cur.isdigit():
            num += cur
        elif cur.isalpha():
            stack[-1][1] += cur
        elif cur == "[":
            if num == "":
                num = 1
            stack.append([int(num), ""])
            num = ""
        elif cur == "]":
            last = stack.pop()
            stack[-1][1] += last[0] * last[1]
    return stack[0][1]


print(solve("3[abc]4[ab]c") == "abcabcabcababababc")
print(solve("2[3[a]b]") == "aaabaaab")
print(solve("a1[cc]b"))
print(solve("1[abc]"))