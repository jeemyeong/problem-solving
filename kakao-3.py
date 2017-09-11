def solution(v):
    x_dict = dict()
    y_dict = dict()
    for x, y in v:
        if x in x_dict.keys():
            x_dict[x] += 1
        else:
            x_dict[x] = 1
        if y in y_dict.keys():
            y_dict[y] += 1
        else:
            y_dict[y] = 1

    answer = []
    for x in x_dict:
        if x_dict[x] == 1:
            answer.append(x)
            break
    for y in y_dict:
        if y_dict[y] == 1:
            answer.append(y)
            break

    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))
