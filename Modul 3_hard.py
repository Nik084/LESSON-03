data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return len(data)

    result = 0
    if isinstance(data, (list, tuple, set)):
        for value in data:
            result += calculate_structure_sum(value)
    elif isinstance(data, dict):
        for key, value in data.items():
            result += calculate_structure_sum(key)
            result += calculate_structure_sum(value)

    return result

result = calculate_structure_sum(data_structure)
print('Result:', result)
