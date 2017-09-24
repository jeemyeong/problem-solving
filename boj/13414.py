def solve(K, L, students):
    student_index_by_id = dict([(student, 0) for student in students])
    for i, student in enumerate(students):
        student_index_by_id[student] = i

    student_id_by_index = dict()
    for student_id in student_index_by_id:
        student_id_by_index[student_index_by_id[student_id]] = student_id
    ret = "\n".join([student_id_by_index[student_id] for student_id in sorted(student_id_by_index)][:K])
    return ret

def run():
    import sys
    read = sys.stdin.readline
    K, L = map(int, read().split())
    students = []
    for _ in range(L):
        students.append(read().replace("\n", ""))
    print(solve(K, L, students))

run()
