def advance(x, func):
    result = func(x)
    return result


print(advance(3, (lambda num: num * 5)))
