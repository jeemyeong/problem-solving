from functools import partial, reduce

def pipe(*fns):
    return partial(reduce, lambda memo, fn: fn(memo), fns)

def tap(cb):
    def fn(x):
        cb(x)
        return x
    return fn

def solve(_input):
    _input = _input[1:len(_input)-1]
    if pipe(partial(filter, lambda x: not x), list, len)(_input.split("/")):
        raise Exception("INVALID INPUT")
    lst = filter(lambda x: x != ".", _input.split("/"))
    def fn(memo, x):
        print(memo, x)
        if x == "..":
            memo.pop()
        else:
            memo.append(x)
        return memo
    lst = reduce(fn, lst, [])
    return "/{}/".format("/".join(lst))

inputs = [
    "/usr/bin/../",
    "/usr/.bin/./test/./"
]

pipe(
    partial(map, solve),
    list,
    "\n".join,
    tap(print),
)(inputs)
