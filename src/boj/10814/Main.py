import sys

def I(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline()

def solve(personal_data_list):
    personal_data_list.sort(key=lambda personal_data: personal_data["age"])
    ret = "\n".join(["%s %s" % (personal_data["age"], personal_data["name"]) for personal_data in personal_data_list])
    return ret

def main():
    N = I()
    personal_data_list = []
    for _ in range(N):
        age, name = map(lambda x: int(x) if x.isdigit() else x, S().split())
        personal_data = {
            "age": age,
            "name": name
        }
        personal_data_list.append(personal_data)

    print(solve(personal_data_list))

main()
