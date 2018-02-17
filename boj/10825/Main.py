import sys
def I(): return int(sys.stdin.readline())

def solve(scores):
    scores.sort(key=lambda x: x["name"])
    scores.sort(key=lambda x: x["math_score"], reverse=True)
    scores.sort(key=lambda x: x["english_score"])
    scores.sort(key=lambda x: x["korean_score"], reverse=True)
    return "\n".join([score["name"] for score in scores])

def main():
    N = I()
    scores = []
    for _ in range(N):
        name, korean_score, english_score, math_score = [int(x) if x.isdigit() else x for x in sys.stdin.readline().split()]
        score = {
            "name": name,
            "korean_score": korean_score,
            "english_score": english_score,
            "math_score": math_score,
        }
        scores.append(score)
    print(solve(scores))

main()
