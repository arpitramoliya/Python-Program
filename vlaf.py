def sum(*args):
    add=0
    for i in args:
        add = i+add
    return add
print(sum(120,140,250,320,110))