calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(m):
    string_ = (len(m), m.upper(), m.lower())
    count_calls()
    return string_
def is_contains(a, b):
    a = a.upper()
    for i in range(len(b)):
        #print (i)
        b[i] = b[i].upper()
        #print(type(b))
        #print(b[i])
    is_cont = a in b
    count_calls()
    return is_cont
print(string_info('sUn+SeT'))
print(string_info('5'))
print(string_info('Hallo, people'))
print(is_contains('banan', ['ban', 'BaNaN', 'URban']))
print(is_contains('UrBan', ['ban', 'BaNaN', 'URban']))
print(is_contains('Urban', ['bant', 'BaNaN', 'URan']))
print(is_contains('Uran', ['uran', 'BaNaN', 'URan']))
print (calls)