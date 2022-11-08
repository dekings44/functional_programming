def multipy_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multipy_by2([8,6,7]))

def square_item(item):
    return item
    
def add_tup(a,b):
    return a + b

#MAP
print(list(map(square_item, [4,5,6])))
x = map(add_tup, ('apple', 'oranges', 'cherry'), ('lemon', 'mango', 'pear'))
print(list(x))

abs_val = map(abs, [-2, 4, -5, -8])
flt = map(float, [-2, 4, -5, -8])
print(list(abs_val))
print(list(flt))

numb = [6, 8, 7, -2, 12]
cubed = map(lambda num: num**3, numb)
print(list(cubed))

#Filter
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, [2,3,4,5,6])))