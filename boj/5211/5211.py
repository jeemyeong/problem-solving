def solve(scale):
    C = 0
    A = 0
    for s in scale:
        if s[0] in 'ADE':
            A += 1
        elif s[0] in 'CFG':
            C += 1
    if A > C:
        return "A-minor"
    elif A < C:
        return "C-major"
    if scale[-1][-1] in 'ADE':
        return "A-minor"
    else:
        return "C-major"
    

def run():
    import sys
    read = sys.stdin.readline

    scale = read().replace(" ", "").replace("\n","").split("|")
    print(solve(scale))

run()
