def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)
values_list = [1, 2.6, [1, 2]]
print_params(*values_list)
values_dict = {'a': 6.1, 'b': 'two', 'c': 10}
print_params(**values_dict)
values_list_2 = ['23', 24]
print_params(*values_list_2)
print_params(*values_list_2, 42)

