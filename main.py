def add(x, **num):
    z = x + num['a'] + num['b'] + num['c']
    print('Addition: ', z)


add(3, a=5, b=2, c=4, d=5)