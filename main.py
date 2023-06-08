def decor(fun):
    def inner():
        a = fun()
        add = a + 5
        return add

    return inner


def num():
    return 10


result_fun = decor(num)
print(result_fun())


@decor
def num():
    return 10


print(num())
