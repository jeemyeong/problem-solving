import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def add_student_to_score(score, student):
    new_score = {
        "score": score["score"],
        "last_min": score["last_min"],
        "last_max": score["last_max"]
    }
    if (new_score["last_min"], new_score["last_max"]) == (-1, -1):
        new_score["last_min"] = student
        new_score["last_max"] = student
    elif student < new_score["last_min"]:
        new_score["score"] += (new_score["last_min"]-student)
        new_score["last_min"] = student
    elif student > new_score["last_max"]:
        new_score["score"] += (student-new_score["last_max"])
        new_score["last_max"] = student
    return new_score

def solve(n, lst):
    include_last_score = {
        "score": 0,
        "last_min": -1,
        "last_max": -1
    }
    exclude_last_score = {
        "score": 0,
        "last_min": -1,
        "last_max": -1
    }
    for student in lst:
        new_exclude_last_score = {
            "score": include_last_score["score"],
            "last_min": student,
            "last_max": student
        }
        include_last_score = add_student_to_score(include_last_score, student)
        exclude_last_score = add_student_to_score(exclude_last_score, student)
        if include_last_score["score"] < exclude_last_score["score"]:
            include_last_score = exclude_last_score
        exclude_last_score = new_exclude_last_score
    return include_last_score["score"]

def main():
    n = I()
    lst = LI()
    print(solve(n, lst))

main()
