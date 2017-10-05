import sys
read = sys.stdin.readline

def solve(h, m, s, t1, t2):
    h = (h % 12 + m/60 + s/3600) * 5
    m = m + s/60
    t1 = (t1 % 12) * 5
    t2 = (t2 % 12) * 5

    a = min(t1, t2)
    b = max(t1, t2)
    h_inner = a < h and h < b
    m_inner = a < m and m < b
    s_inner = a < s and s < b
    if h_inner and m_inner and s_inner:
        return "YES"
    if not h_inner and not m_inner and not s_inner:
        return "YES"
    return "NO"

def run():
    h, m, s, t1, t2 = list(map(int, read().replace("\n", "").split()))
    print(solve(h, m, s, t1, t2))

run()