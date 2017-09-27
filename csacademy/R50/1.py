def solve(word):
    dic = dict([('N', 0), ('E', 0), ('S', 0), ('W', 0)])
    for char in list(word):
        dic[char] += 1
    width = abs(dic['E'] - dic['W'])
    height = abs(dic['N'] - dic['S'])
    return width + height

def parser():
    while 1:
        data = input()
        yield(data)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(solve(data))
    except ValueError:
        return float(data)

print(get_number())
