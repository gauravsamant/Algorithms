def f(x):
    def g():
        x = 'abc'
        print(f'In G => X = {x}.')
    def h():
        z = x
        print(f'In H => Z = {z}')
    x = x + 1
    print(f'In F => X = {x}')
    h()
    g()
    print(f'X = {x}')
    return g

x = 3
z = f(x)
print('Outer Loop')
print(f'X = {x}')
print(f'Z = {z}')
z()