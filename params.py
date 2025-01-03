def print_params (a = 1, b = 'string', c = True):
    print(a, b, c)

value_list = ['object', 54.36, 16]
value_dict = {'a' : 15, 'b' : 'file', 'c' : False}


print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*value_list)
print_params(**value_dict)


value_list = ['Play', 85]
print_params(*value_list, 42)