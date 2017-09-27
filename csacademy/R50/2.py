# Not solved
def solve(word):
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    index = day_of_week.index(word.replace("\n", ""))
    first_friday = 7 - index
    cnt = 0
    for days_of_each_month in days_of_month:
        second_friday = first_friday + 7
        if second_friday == 13:
            cnt+=1
        first_friday += days_of_each_month-28
        if first_friday > 7:
            first_friday %= 7
    return cnt

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
