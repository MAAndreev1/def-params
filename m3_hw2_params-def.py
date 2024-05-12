def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2, 3)
print_params('a')
print_params(a=3, b=2, c=1)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'str', True]
values_dict = {'a': 1, 'b': 'str', 'c': False}

print('-----------------')
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 'one']

print('-----------------')
print_params(*values_list_2, 42)
