def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func


add_5 = outer_func(5)
add_10 = outer_func(10)

print(add_5(3))
print(add_10(3))